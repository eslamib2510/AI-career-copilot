from data_loader import jobs_df

# ====================================
# SKILL GAP ANALYSIS
# ====================================

def analyze_skill_gap(
    detected_skills,
    recommended_jobs
):

    required_skills = set()

    # Collect skills from recommended jobs
    for job in recommended_jobs:

        matched_jobs = jobs_df[
            jobs_df["title"] == job["title"]
        ]

        for _, row in matched_jobs.iterrows():

            skill = row["skill_name"]

            if isinstance(skill, str):

                required_skills.add(
                    skill.lower()
                )

    # User skills
    user_skills = set(
        [
            skill.lower()

            for skill in detected_skills
        ]
    )

    # Missing skills
    missing_skills = required_skills - user_skills

    return list(missing_skills)