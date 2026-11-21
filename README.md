# AI resume screening system

Sqrock IT Solutions, Data Science internship, Phase 1, Task 3.

This project reads resumes (PDF or TXT), compares them with a job description using NLP, and ranks the candidates by match score. Candidates under the threshold are filtered out.

## Run it

```bash
pip install -r requirements.txt
python generate_data.py                # creates sample resumes and a job description
python main.py                         # ranking list in the terminal and in outputs/
python main.py --threshold 60          # stricter shortlist
python main.py --resumes my_folder --jd my_jd.txt   # your own files
streamlit run app.py                   # web app with file upload
```

No NLTK downloads are needed. The project uses NLTK's Porter stemmer, which works offline.

## Dataset

`data/resumes/` has 15 made-up resumes (11 TXT, 4 PDF) for different roles, so the ranking has some clear mismatches (accountant, network admin, designer, and so on). `data/job_description.txt` is a Junior Data Scientist posting.

## What each step does

1. Data collection: reads TXT directly and PDFs with pypdf.
2. Preprocessing: lowercase, remove emails, punctuation and digits, tokenize, remove stopwords, stem.
3. Feature extraction: TF-IDF with 1 and 2 word n-grams (default), or Bag of Words with `--method bow`.
4. Matching: cosine similarity between each resume and the job description, plus keyword matching against a skill list.
5. Ranking: final score = 60% scaled cosine similarity + 40% share of the job's skills found in the resume. Resumes below the threshold (default 50%) are rejected.
6. Output: candidate name, match score %, rank, status, matched and missing skills, a rough experience estimate and education level. Saved to `outputs/ranking.csv`, `outputs/shortlisted.csv` and `outputs/match_scores.png`.

## Sample result

Top of the ranking with the default settings: Ayesha Malik (87.1%), Ali Hassan (82.1%), Hamza Raza (78.3%), Iqra Javed (75.1%). The lowest are Talha Mehmood (1.1%) and Maryam Iqbal (2.9%), whose resumes have almost nothing in common with the job. 8 of 15 candidates are shortlisted.

The experience figure is a regex guess from phrases like "2 years" and "8 months", so treat it as a hint and not a fact. The skill list in `screening.py` is easy to extend.

## Files

- `screening.py`: reading, preprocessing, extraction, scoring
- `main.py`: command line pipeline
- `app.py`: Streamlit app
- `generate_data.py`: builds the sample resumes and job description

## Deploy

Push to GitHub and create a Streamlit Community Cloud app with `app.py` as the main file.
