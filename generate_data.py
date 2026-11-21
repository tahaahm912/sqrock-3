"""Creates sample resumes (TXT and PDF) and a job description in data/.

All names and details are made up. Run:  python generate_data.py
"""
from pathlib import Path

DATA = Path(__file__).parent / "data"

JOB_DESCRIPTION = """Job Title: Junior Data Scientist

We are looking for a Junior Data Scientist to join our analytics team. You will clean and analyze
business data, build machine learning models and present results to non-technical colleagues.

Responsibilities:
- Collect, clean and preprocess data using Python, Pandas and NumPy
- Run exploratory data analysis and build charts with Matplotlib and Seaborn
- Build, train and evaluate machine learning models with Scikit-learn (regression, classification, clustering)
- Write SQL queries to pull data from relational databases
- Work with NLP techniques such as TF-IDF and text classification
- Share findings in Jupyter notebooks and dashboards (Power BI or Tableau)
- Use Git and GitHub for version control

Requirements:
- Bachelor's degree in Computer Science, Data Science, Statistics or a related field
- 1 to 3 years of experience in data analysis or machine learning (internships count)
- Strong knowledge of Python, statistics and machine learning
- Good communication and problem solving skills
- Nice to have: deep learning (TensorFlow or PyTorch), Streamlit, Docker
"""

RESUMES = {
    "Ayesha_Malik": """Ayesha Malik
Email: ayesha.malik@example.com | Lahore, Pakistan
Education: BS Data Science, University of Engineering and Technology Lahore (CGPA 3.6)
Experience: Data Science Intern, 8 months, at a retail analytics startup. Cleaned sales data with Python, Pandas and NumPy,
built regression and classification models in Scikit-learn, and wrote SQL queries for reporting. Created dashboards in Power BI.
Projects: Customer churn prediction with Random Forest, resume classifier using TF-IDF and NLP, sales forecasting in Jupyter.
Skills: Python, Pandas, NumPy, Scikit-learn, SQL, Matplotlib, Seaborn, machine learning, statistics, NLP, TF-IDF, Power BI, Git, GitHub, Streamlit
""",
    "Hamza_Raza": """Hamza Raza
Email: hamza.raza@example.com | Islamabad, Pakistan
Education: BS Computer Science, FAST NUCES (CGPA 3.3)
Experience: Machine Learning Intern for 6 months. Trained classification models, tuned hyperparameters, and deployed a model
with Streamlit and Docker. Worked with Pandas, NumPy and Scikit-learn every day. Used Git and GitHub for team projects.
Projects: Image classifier in TensorFlow, loan default prediction, text classification with TF-IDF.
Skills: Python, machine learning, Scikit-learn, TensorFlow, deep learning, Pandas, NumPy, SQL, Docker, Streamlit, Git, GitHub, NLP, Jupyter
""",
    "Sana_Tariq": """Sana Tariq
Email: sana.tariq@example.com | Karachi, Pakistan
Education: MS Statistics, University of Karachi
Experience: Data Analyst for 2 years at a bank. Wrote SQL queries, built Tableau dashboards, ran statistical tests and regression analysis
in Python and Pandas. Presented monthly findings to management.
Projects: Credit risk analysis, A/B testing report, exploratory data analysis of customer transactions.
Skills: Python, SQL, Tableau, statistics, Pandas, NumPy, Matplotlib, Seaborn, regression, data analysis, Excel, communication, problem solving
""",
    "Bilal_Ahmed": """Bilal Ahmed
Email: bilal.ahmed@example.com | Lahore, Pakistan
Education: BS Software Engineering, UET Lahore
Experience: Full stack developer for 2 years. Built web apps with React, Node.js and MongoDB. Some experience with Python scripts for automation.
Projects: E-commerce website, chat application, REST API with Express.
Skills: JavaScript, React, Node.js, MongoDB, HTML, CSS, Git, GitHub, REST API, Python, Docker
""",
    "Fatima_Noor": """Fatima Noor
Email: fatima.noor@example.com | Faisalabad, Pakistan
Education: BBA Marketing, GC University Faisalabad
Experience: Digital marketing executive for 3 years. Ran Facebook and Google ad campaigns, wrote content, managed social media accounts and
reported weekly campaign numbers in Excel.
Projects: Brand launch campaign, SEO audit, email marketing automation.
Skills: SEO, social media, Google Ads, Facebook Ads, content writing, Excel, Canva, communication, copywriting
""",
    "Usman_Sheikh": """Usman Sheikh
Email: usman.sheikh@example.com | Lahore, Pakistan
Education: BS Computer Science, COMSATS University (CGPA 3.1)
Experience: 4 months internship in data analysis. Used Python, Pandas and Matplotlib to clean and visualize datasets. Basic Scikit-learn models
(linear regression, decision tree). Built a Power BI report for a university society.
Projects: Student performance predictor, Titanic survival prediction, COVID-19 data dashboard.
Skills: Python, Pandas, NumPy, Matplotlib, Scikit-learn, Power BI, SQL, Jupyter, Git, machine learning
""",
    "Maryam_Iqbal": """Maryam Iqbal
Email: maryam.iqbal@example.com | Lahore, Pakistan
Education: BS Design, National College of Arts
Experience: UI/UX designer for 2 years. Designed mobile app screens in Figma, ran user interviews and built clickable prototypes.
Projects: Food delivery app redesign, banking app wireframes, design system for a startup.
Skills: Figma, Adobe XD, wireframing, prototyping, user research, UI design, UX design, Photoshop, Illustrator, communication
""",
    "Ali_Hassan": """Ali Hassan
Email: ali.hassan@example.com | Rawalpindi, Pakistan
Education: BS Data Science, NUST (CGPA 3.8)
Experience: Research assistant for 1 year working on deep learning for medical images with PyTorch. Data Science intern for 6 months, built churn and
forecasting models with Scikit-learn, wrote SQL, and used Git and GitHub. Presented results to the team every two weeks.
Projects: Chest X-ray classifier (PyTorch), demand forecasting, NLP sentiment analysis with TF-IDF and logistic regression.
Skills: Python, PyTorch, deep learning, machine learning, Scikit-learn, Pandas, NumPy, SQL, NLP, statistics, Matplotlib, Seaborn, Jupyter, Git, GitHub, Docker
""",
    "Zainab_Khan": """Zainab Khan
Email: zainab.khan@example.com | Multan, Pakistan
Education: BCom, Bahauddin Zakariya University
Experience: Accountant for 4 years. Prepared financial statements, handled payroll and tax filing, worked in QuickBooks and Excel.
Skills: Accounting, QuickBooks, Excel, taxation, payroll, financial reporting, communication
""",
    "Hassan_Butt": """Hassan Butt
Email: hassan.butt@example.com | Lahore, Pakistan
Education: BS Computer Science, University of the Punjab
Experience: Junior Python developer for 1 year. Wrote backend services in Django, worked with PostgreSQL and SQL, and wrote a few data cleaning scripts
with Pandas. Completed an online machine learning course and built two small Scikit-learn projects.
Projects: Inventory management system (Django), house price prediction, web scraper.
Skills: Python, Django, PostgreSQL, SQL, Pandas, Scikit-learn, Git, GitHub, REST API, machine learning
""",
    "Nimra_Aslam": """Nimra Aslam
Email: nimra.aslam@example.com | Sialkot, Pakistan
Education: BS Mathematics, Government College University
Experience: Math tutor for 3 years. Fresh graduate in data science courses. Completed Python, statistics and machine learning online courses.
Projects: Linear regression on housing data, iris classification, simple Jupyter notebooks.
Skills: Python, statistics, mathematics, Pandas, NumPy, Matplotlib, Jupyter, machine learning basics, communication
""",
    "Talha_Mehmood": """Talha Mehmood
Email: talha.mehmood@example.com | Lahore, Pakistan
Education: BS Information Technology, University of Lahore
Experience: Network administrator for 3 years. Managed routers, switches, firewalls and VPN setup. Troubleshot network outages.
Skills: Networking, Cisco, firewall, VPN, Linux, troubleshooting, Windows Server, CCNA
""",
    "Iqra_Javed": """Iqra Javed
Email: iqra.javed@example.com | Lahore, Pakistan
Education: MS Computer Science, LUMS
Experience: Data Scientist for 2 years at a fintech company. Built fraud detection models (Random Forest, XGBoost) with Scikit-learn, wrote SQL for
feature pipelines, ran NLP text classification with TF-IDF, and built Streamlit tools for analysts. Used Docker, Git and GitHub. Mentored two interns.
Projects: Fraud detection system, customer segmentation with clustering, topic modelling on support tickets.
Skills: Python, machine learning, Scikit-learn, XGBoost, Pandas, NumPy, SQL, NLP, TF-IDF, clustering, statistics, Streamlit, Docker, Git, GitHub, Tableau, Jupyter, TensorFlow
""",
    "Danish_Ali": """Danish Ali
Email: danish.ali@example.com | Peshawar, Pakistan
Education: BS Electrical Engineering, UET Peshawar
Experience: Embedded systems engineer for 2 years. Wrote C and C++ firmware for microcontrollers, designed circuits, and tested sensors.
Skills: C, C++, embedded systems, Arduino, circuit design, MATLAB, communication
""",
    "Rabia_Siddiqui": """Rabia Siddiqui
Email: rabia.siddiqui@example.com | Lahore, Pakistan
Education: BS Statistics, Forman Christian College (CGPA 3.5)
Experience: Data analytics intern for 5 months. Cleaned survey data in Python and Pandas, built regression models, created Tableau dashboards, and wrote
SQL queries. Learned Scikit-learn and Git during the internship.
Projects: Survey analysis, student dropout prediction, sales dashboard.
Skills: Python, Pandas, NumPy, SQL, Tableau, statistics, regression, Scikit-learn, Matplotlib, Seaborn, Git, communication
""",
}


def write_pdf(path, text):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    styles = getSampleStyleSheet()
    story = []
    for line in text.strip().split("\n"):
        story += [Paragraph(line.replace("&", "&amp;"), styles["Normal"]), Spacer(1, 6)]
    SimpleDocTemplate(str(path), pagesize=A4).build(story)


def build():
    res_dir = DATA / "resumes"
    res_dir.mkdir(parents=True, exist_ok=True)
    (DATA / "job_description.txt").write_text(JOB_DESCRIPTION, encoding="utf-8")
    pdf_names = {"Ayesha_Malik", "Iqra_Javed", "Bilal_Ahmed", "Fatima_Noor"}  # a few as PDF to test the parser
    pdf_ok = True
    for name, text in RESUMES.items():
        if name in pdf_names:
            try:
                write_pdf(res_dir / f"{name}.pdf", text)
                continue
            except ImportError:
                pdf_ok = False
        (res_dir / f"{name}.txt").write_text(text, encoding="utf-8")
    print(f"Created {len(RESUMES)} sample resumes in {res_dir}" + ("" if pdf_ok else " (reportlab missing, all TXT)"))


if __name__ == "__main__":
    build()
