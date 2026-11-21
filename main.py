"""AI Resume Screening System: ranks resumes against a job description.

Run:  python main.py
Optional:  python main.py --resumes my_folder --jd my_jd.txt --threshold 50
"""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

import screening as sc

ROOT = Path(__file__).parent
parser = argparse.ArgumentParser()
parser.add_argument("--resumes", default=str(ROOT / "data" / "resumes"), help="folder with PDF/TXT resumes")
parser.add_argument("--jd", default=str(ROOT / "data" / "job_description.txt"), help="job description TXT file")
parser.add_argument("--threshold", type=float, default=50.0, help="minimum match score (%%) to shortlist")
parser.add_argument("--method", choices=["tfidf", "bow"], default="tfidf")
args = parser.parse_args()

OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")

# %% 1. Data collection
if not Path(args.resumes).exists() or not any(Path(args.resumes).glob("*")):
    import generate_data
    generate_data.build()
resumes = sc.load_resumes(args.resumes)
jd = Path(args.jd).read_text(encoding="utf-8")
print(f"Loaded {len(resumes)} resumes ({sum(resumes['File'].str.endswith('.pdf'))} PDF, "
      f"{sum(resumes['File'].str.endswith('.txt'))} TXT)")

# %% 2-5. Preprocess, vectorize, match, rank
ranked, jd_skills = sc.rank_resumes(resumes, jd, threshold=args.threshold, method=args.method)
print(f"\nSkills required by the job description: {', '.join(jd_skills)}")

# %% 6. Output
show = ranked[["Rank", "Candidate", "Match Score %", "Keyword Match %", "Experience (yrs)", "Education", "Status"]]
print("\nRANKING LIST")
print(show.to_string(index=False))

short = ranked[ranked["Status"] == "Shortlisted"]
print(f"\nSHORTLISTED CANDIDATES ({len(short)})")
for _, r in short.iterrows():
    print(f"  #{r['Rank']} {r['Candidate']}: {r['Match Score %']}%  | missing: {', '.join(r['Missing Skills']) or 'none'}")

out = ranked.drop(columns=["Text", "Clean"]).copy()
for col in ["Skills Found", "Matched Skills", "Missing Skills"]:
    out[col] = out[col].apply(lambda x: ", ".join(x))
out.to_csv(OUT / "ranking.csv", index=False)
short_out = out[out["Status"] == "Shortlisted"]
short_out.to_csv(OUT / "shortlisted.csv", index=False)

fig, ax = plt.subplots(figsize=(9, max(4, len(ranked) * 0.38)))
colors = ["#2ca02c" if s == "Shortlisted" else "#c7c7c7" for s in ranked["Status"]]
ax.barh(ranked["Candidate"][::-1], ranked["Match Score %"][::-1], color=colors[::-1])
ax.axvline(args.threshold, color="red", ls="--", label=f"Threshold ({args.threshold:.0f}%)")
ax.set(title="Resume match scores", xlabel="Match score (%)"); ax.legend(loc="lower right")
fig.tight_layout(); fig.savefig(OUT / "match_scores.png", dpi=130); plt.close(fig)
print(f"\nSaved ranking.csv, shortlisted.csv and match_scores.png to {OUT}")
