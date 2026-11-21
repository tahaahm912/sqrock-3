"""Streamlit app for the AI Resume Screening System. Run:  streamlit run app.py"""
from pathlib import Path
import pandas as pd
import streamlit as st

import generate_data
import screening as sc

st.set_page_config(page_title="AI Resume Screening", layout="wide")
ROOT = Path(__file__).parent
st.title("AI Resume Screening System")
st.caption("Ranks resumes by how well they match a job description (TF-IDF + cosine similarity + skill matching).")

default_jd = (ROOT / "data" / "job_description.txt")
if not default_jd.exists():
    generate_data.build()

jd = st.text_area("Job description", default_jd.read_text(encoding="utf-8"), height=260)
files = st.file_uploader("Upload resumes (PDF or TXT)", type=["pdf", "txt"], accept_multiple_files=True)
use_sample = st.checkbox("Use the sample resumes", value=not files)
threshold = st.slider("Shortlist threshold (match score %)", 10, 90, 50)
method = st.radio("Feature extraction", ["tfidf", "bow"], horizontal=True,
                  format_func=lambda m: "TF-IDF (recommended)" if m == "tfidf" else "Bag of Words")

rows = []
for f in files or []:
    text = sc.read_pdf(f) if f.name.lower().endswith(".pdf") else f.read().decode("utf-8", errors="ignore")
    rows.append({"Candidate": Path(f.name).stem.replace("_", " "), "File": f.name, "Text": text})
if use_sample:
    rows += sc.load_resumes(ROOT / "data" / "resumes").to_dict("records")

if st.button("Screen resumes", type="primary"):
    if not rows or not jd.strip():
        st.warning("Add a job description and at least one resume.")
        st.stop()
    ranked, jd_skills = sc.rank_resumes(pd.DataFrame(rows), jd, threshold=threshold, method=method)
    st.write("Skills found in the job description:", ", ".join(jd_skills))
    show = ranked[["Rank", "Candidate", "Match Score %", "Keyword Match %", "Experience (yrs)", "Education", "Status"]]
    st.subheader("Ranking list")
    st.dataframe(show, width="stretch", hide_index=True)
    st.bar_chart(ranked.set_index("Candidate")["Match Score %"])
    short = ranked[ranked["Status"] == "Shortlisted"]
    st.subheader(f"Shortlisted candidates ({len(short)})")
    for _, r in short.iterrows():
        with st.expander(f"#{r['Rank']}  {r['Candidate']}  -  {r['Match Score %']}%"):
            st.write("Matched skills:", ", ".join(r["Matched Skills"]) or "none")
            st.write("Missing skills:", ", ".join(r["Missing Skills"]) or "none")
    st.download_button("Download ranking CSV", show.to_csv(index=False), "ranking.csv")
