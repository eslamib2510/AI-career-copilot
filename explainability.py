
# ====================================
# JOB SKILLS DATABASE
# ====================================

job_skills = {

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
# EXPLAINABLE AI
# ====================================

def explain_recommendation(

    user_skills,

    job_title
):

    required_skills = job_skills.get(
        job_title,
        []
    )

    matched_skills = [

        skill

        for skill in user_skills

        if skill in required_skills
    ]

    return matched_skills

