
# ====================================
# REQUIRED SKILLS DATABASE
# ====================================

required_skills = {

    "Machine Learning Engineer": [

        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "NLP",
        "AI"
    ],

    "Data Scientist": [

        "Python",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Data Analysis"
    ],

    "AI Engineer": [

        "Python",
        "PyTorch",
        "Transformers",
        "Deep Learning",
        "NLP"
    ],

    "Backend Developer": [

        "Python",
        "FastAPI",
        "APIs",
        "SQL",
        "Backend Development"
    ],

    "Data Analyst": [

        "Excel",
        "SQL",
        "Power BI",
        "Statistics",
        "Data Visualization"
    ]
}

# ====================================
# SKILL GAP ANALYSIS
# ====================================

def analyze_skill_gap(

    detected_skills,

    recommended_jobs
):

    missing_skills = set()

    for job in recommended_jobs:

        job_title = job["title"]

        job_required_skills = required_skills.get(
            job_title,
            []
        )

        for skill in job_required_skills:

            if skill not in detected_skills:

                missing_skills.add(skill)

    return list(missing_skills)

