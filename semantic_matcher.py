from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ====================================
# SAMPLE JOB DATABASE
# ====================================

jobs = [

    {
        "title": "Machine Learning Engineer",
        "company": "Google",
        "location": "Remote",
        "salary": "$120,000",

        "description":
        "Python Machine Learning Deep Learning TensorFlow NLP AI"
    },

    {
        "title": "Data Scientist",
        "company": "Microsoft",
        "location": "Remote",
        "salary": "$110,000",

        "description":
        "Python Data Analysis SQL Machine Learning Statistics"
    },

    {
        "title": "AI Engineer",
        "company": "OpenAI",
        "location": "Remote",
        "salary": "$150,000",

        "description":
        "LLM NLP Deep Learning Transformers PyTorch AI"
    },

    {
        "title": "Backend Developer",
        "company": "Amazon",
        "location": "Hybrid",
        "salary": "$100,000",

        "description":
        "Python APIs SQL FastAPI Backend Development"
    },

    {
        "title": "Data Analyst",
        "company": "IBM",
        "location": "On-site",
        "salary": "$90,000",

        "description":
        "Excel SQL Power BI Data Visualization Statistics"
    }

]

# ====================================
# SEMANTIC MATCHING
# ====================================

def semantic_job_search(
    resume_text
):

    job_descriptions = [

        job["description"]

        for job in jobs
    ]

    corpus = [

        resume_text

    ] + job_descriptions

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(
        corpus
    )

    similarity_scores = cosine_similarity(

        tfidf_matrix[0:1],

        tfidf_matrix[1:]

    )[0]

    recommended_jobs = []

    for idx, score in enumerate(
        similarity_scores
    ):

        recommended_jobs.append({

            "title":
            jobs[idx]["title"],

            "company":
            jobs[idx]["company"],

            "location":
            jobs[idx]["location"],

            "salary":
            jobs[idx]["salary"],

            "match":
            round(score * 100, 2)
        })

    recommended_jobs = sorted(

        recommended_jobs,

        key=lambda x: x["match"],

        reverse=True
    )

    return recommended_jobs[:5]
