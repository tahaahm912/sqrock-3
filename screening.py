"""Core logic for the AI Resume Screening System (used by main.py and app.py)."""
import re
from pathlib import Path

import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

STEMMER = PorterStemmer()
STOPWORDS = set(ENGLISH_STOP_WORDS)

# Skill vocabulary used for keyword matching (lowercase). Multi-word skills are matched as phrases.
SKILLS = [
    "python", "pandas", "numpy", "scikit-learn", "sklearn", "matplotlib", "seaborn", "sql", "mysql", "postgresql",
    "machine learning", "deep learning", "nlp", "tf-idf", "statistics", "tensorflow", "pytorch", "keras", "xgboost",
    "jupyter", "streamlit", "docker", "git", "github", "power bi", "tableau", "excel", "regression", "classification",
    "clustering", "data analysis", "data science", "data visualization", "communication", "problem solving",
    "java", "javascript", "react", "node.js", "django", "flask", "html", "css", "mongodb", "figma", "seo",
    "networking", "accounting", "c++",
]


# ---------- 1. Data collection ----------
def read_pdf(source):
    """Extracts text from a PDF path or file-like object using pypdf (falls back to PyPDF2)."""
    try:
        from pypdf import PdfReader
    except ImportError:
        from PyPDF2 import PdfReader
    reader = PdfReader(source)
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def read_resume(path):
    path = Path(path)
    if path.suffix.lower() == ".pdf":
        return read_pdf(str(path))
    return path.read_text(encoding="utf-8", errors="ignore")


def load_resumes(folder):
    rows = []
    for p in sorted(Path(folder).glob("*")):
        if p.suffix.lower() in {".pdf", ".txt"}:
            rows.append({"Candidate": p.stem.replace("_", " "), "File": p.name, "Text": read_resume(p)})
    return pd.DataFrame(rows)


# ---------- 2. Preprocessing ----------
def preprocess(text):
    """Lowercase, strip emails/punctuation/numbers, tokenize, drop stopwords, stem."""
    text = text.lower()
    text = re.sub(r"\S+@\S+", " ", text)                  # emails
    text = re.sub(r"[^a-z\s+#]", " ", text)               # punctuation, digits, special characters
    tokens = [t for t in text.split() if len(t) > 1 and t not in STOPWORDS]
    return " ".join(STEMMER.stem(t) for t in tokens)


# ---------- Info extraction (skills, experience, education) ----------
def find_skills(text):
    t = " " + text.lower() + " "
    found = []
    for s in SKILLS:
        pattern = r"(?<![a-z0-9])" + re.escape(s) + r"(?![a-z0-9])"
        if re.search(pattern, t):
            found.append(s)
    return found


def extract_years(text):
    """Rough estimate of experience in years from phrases like '2 years' or '8 months'."""
    years = [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*(?:\+\s*)?years?", text.lower())]
    months = [float(x) for x in re.findall(r"(\d+)\s*months?", text.lower())]
    total = sum(years) + sum(months) / 12
    return round(min(total, 15), 1)


def extract_education(text):
    """Highest degree level found in the text (word-boundary match, so 'systems' is not 'ms')."""
    t = text.lower()
    if re.search(r"\bph\.?d\b|\bdoctorate\b", t):
        return "PhD"
    if re.search(r"\b(ms|msc|m\.sc|mba|mphil|master'?s?)\b", t):
        return "Master's"
    if re.search(r"\b(bs|bsc|b\.sc|bba|bcom|be|beng|bachelor'?s?)\b", t):
        return "Bachelor's"
    return "Not found"


# ---------- 3-4. Feature extraction and matching ----------
def vectorize(clean_resumes, clean_jd, method="tfidf"):
    if method == "bow":
        vec = CountVectorizer(ngram_range=(1, 2))
    else:
        vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
    matrix = vec.fit_transform(list(clean_resumes) + [clean_jd])
    return matrix[:-1], matrix[-1]


def rank_resumes(resumes, job_description, threshold=40.0, method="tfidf",
                 w_similarity=0.6, w_keywords=0.4):
    """Scores every resume against the job description.

    Final score = w_similarity * cosine similarity (scaled) + w_keywords * keyword match.
    Cosine similarity between a long job description and a resume is usually small (0.1 to 0.5),
    so it is divided by the best similarity in the batch before mixing. Keyword match is the share
    of the job description's skills that the resume mentions.
    """
    df = resumes.copy()
    clean_jd = preprocess(job_description)
    df["Clean"] = df["Text"].apply(preprocess)
    res_matrix, jd_vec = vectorize(df["Clean"], clean_jd, method)

    sim = cosine_similarity(res_matrix, jd_vec).ravel()
    sim_scaled = sim / sim.max() if sim.max() > 0 else sim

    jd_skills = find_skills(job_description)
    df["Skills Found"] = df["Text"].apply(find_skills)
    df["Matched Skills"] = df["Skills Found"].apply(lambda s: [k for k in s if k in jd_skills])
    df["Missing Skills"] = df["Matched Skills"].apply(lambda m: [k for k in jd_skills if k not in m])
    kw = df["Matched Skills"].apply(len) / max(len(jd_skills), 1)

    df["Cosine Similarity"] = sim.round(4)
    df["Keyword Match %"] = (kw * 100).round(1)
    df["Match Score %"] = ((w_similarity * sim_scaled + w_keywords * kw) * 100).round(1)
    df["Experience (yrs)"] = df["Text"].apply(extract_years)
    df["Education"] = df["Text"].apply(extract_education)

    df = df.sort_values("Match Score %", ascending=False).reset_index(drop=True)
    df.insert(0, "Rank", np.arange(1, len(df) + 1))
    df["Status"] = np.where(df["Match Score %"] >= threshold, "Shortlisted", "Rejected (low score)")
    return df, jd_skills
