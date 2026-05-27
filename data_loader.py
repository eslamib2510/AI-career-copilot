import pandas as pd

# =========================
# LOAD DATASETS
# =========================

postings_df = pd.read_csv(
    "data/postings.csv"
)

job_skills_df = pd.read_csv(
    "data/job_skills.csv"
)

skills_df = pd.read_csv(
    "data/skills.csv"
)

companies_df = pd.read_csv(
    "data/companies.csv"
)

industries_df = pd.read_csv(
    "data/industries.csv"
)

salaries_df = pd.read_csv(
    "data/salaries.csv"
)

benefits_df = pd.read_csv(
    "data/benefits.csv"
)

# =========================
# NORMALIZE SKILLS
# =========================

job_skills_df = job_skills_df.merge(
    skills_df,
    on="skill_abr",
    how="left"
)

# =========================
# MERGE JOB DATA
# =========================

jobs_df = job_skills_df.merge(
    postings_df,
    on="job_id",
    how="left"
)

# =========================
# FINAL CLEAN DATASET
# =========================

jobs_df = jobs_df[
    [
        "job_id",
        "title",
        "description",
        "company_name",
        "formatted_experience_level",
        "location",
        "normalized_salary",
        "skill_name"
    ]
]