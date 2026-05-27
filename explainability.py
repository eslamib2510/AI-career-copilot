from data_loader import jobs_df

# ====================================
# EXPLAIN RECOMMENDATIONS
# ====================================

def explain_recommendation(

    detected_skills,

    job_title
):

    matched_skills = []

    # Get matching jobs
    matched_jobs = jobs_df[
        jobs_df["title"] == job_title
    ]

    # Extract job skills
    job_skills = set()

    for _, row in matched_jobs.iterrows():

        skill = row["skill_name"]

        if isinstance(skill, str):

            job_skills.add(
                skill.lower()
            )

    # Compare with resume skills
    for skill in detected_skills:

        if skill.lower() in job_skills:

            matched_skills.append(
                skill
            )

    return matched_skills