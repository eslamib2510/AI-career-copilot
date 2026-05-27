import matplotlib.pyplot as plt

# ====================================
# JOB MATCH VISUALIZATION
# ====================================

def plot_job_matches(
    recommended_jobs
):

    job_titles = [
        job["title"]
        for job in recommended_jobs[:5]
    ]

    match_scores = [
        job["match"]
        for job in recommended_jobs[:5]
    ]

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.barh(
        job_titles,
        match_scores
    )

    ax.set_xlabel(
        "Match Score"
    )

    ax.set_title(
        "Top Recommended Jobs"
    )

    plt.tight_layout()

    return fig