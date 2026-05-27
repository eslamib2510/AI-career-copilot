import pandas as pd

# Load skills dataset
skills_df = pd.read_csv(
    "data/skills.csv"
)

# Get all skills
REAL_SKILLS = skills_df[
    "skill_name"
].dropna().str.lower().tolist()


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in REAL_SKILLS:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))