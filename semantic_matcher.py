from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from data_loader import jobs_df

# =========================
# CLEAN DATA
# =========================

jobs_df = jobs_df.dropna(
    subset=["description"]
)

jobs_df = jobs_df.drop_duplicates(
    subset=["job_id"]
)

# =========================
# TF-IDF
# =========================

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

job_vectors = vectorizer.fit_transform(
    jobs_df["description"]
)

# =========================
# SEARCH FUNCTION
# =========================

def semantic_job_search(
    resume_text
):

    resume_vector = vectorizer.transform(
        [resume_text]
    )

    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    top_indices = similarities.argsort()[-10:][::-1]

    recommendations = []

    for idx in top_indices:

        job = jobs_df.iloc[idx]

        recommendations.append({

            "title":
                job["title"],

            "company":
                job["company_name"],

            "location":
                job["location"],

            "salary":
                job["normalized_salary"],

            "match":
                round(
                    similarities[idx] * 100,
                    2
                )
        })

    return recommendations