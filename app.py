import streamlit as st
import os
import joblib

from parser import extract_text_from_pdf
from skills import extract_skills
from ats import calculate_ats_score

from semantic_matcher import (
    semantic_job_search
)

from explainability import (
    explain_recommendation
)

from skill_gap import (
    analyze_skill_gap
)

from visualizations import (
    plot_job_matches
)

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="AI Resume Intelligence System",
    page_icon="📄",
    layout="wide"
)

# ====================================
# CACHE MODELS
# ====================================

@st.cache_resource
def load_models():

    model = joblib.load(
        "resume_classifier.pkl"
    )

    vectorizer = joblib.load(
        "tfidf_vectorizer.pkl"
    )

    return model, vectorizer

model, vectorizer = load_models()

# ====================================
# CUSTOM CSS
# ====================================

st.markdown("""
<style>

html, body, [class*="css"] {

    font-family: 'Segoe UI', sans-serif;
}

.main {

    background-color: #0F172A;

    color: white;
}

.block-container {

    padding-top: 2rem;

    padding-bottom: 2rem;

    padding-left: 3rem;

    padding-right: 3rem;
}

.hero-box {

    background: linear-gradient(
        135deg,
        #1E293B,
        #0F172A
    );

    padding: 40px;

    border-radius: 25px;

    border: 1px solid #334155;

    margin-bottom: 30px;
}

.hero-title {

    font-size: 42px;

    font-weight: bold;

    color: white;
}

.hero-subtitle {

    font-size: 18px;

    color: #CBD5E1;

    margin-top: 15px;

    line-height: 1.8;
}

.section-header {

    font-size: 28px;

    font-weight: bold;

    margin-top: 15px;

    margin-bottom: 20px;

    color: white;
}

.skill-box {

    background-color: #1E293B;

    padding: 12px;

    border-radius: 12px;

    text-align: center;

    border: 1px solid #334155;

    margin-bottom: 10px;

    color: white;

    font-weight: 500;
}

.job-card {

    background-color: #111827;

    padding: 25px;

    border-radius: 20px;

    border: 1px solid #374151;

    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title(
    "AI Resume Intelligence"
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Machine Learning Pipeline"
)

st.sidebar.write(
    "• NLP Preprocessing"
)

st.sidebar.write(
    "• TF-IDF Vectorization"
)

st.sidebar.write(
    "• Logistic Regression"
)

st.sidebar.write(
    "• Semantic Similarity"
)

st.sidebar.write(
    "• Explainable AI"
)

st.sidebar.write(
    "• Skill Gap Analysis"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Built using AI, NLP, and Machine Learning concepts."
)

# ====================================
# HERO SECTION
# ====================================

st.markdown("""
<div class="hero-box">

<div class="hero-title">
AI Resume Intelligence System
</div>

<div class="hero-subtitle">

Analyze resumes using:
<br><br>

• Natural Language Processing (NLP)
<br>

• Machine Learning Classification
<br>

• Semantic Recommendation Systems
<br>

• Explainable AI Techniques
<br>

• Skill Gap Analysis

</div>

</div>
""", unsafe_allow_html=True)

# ====================================
# FILE UPLOADER
# ====================================

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ====================================
# MAIN PIPELINE
# ====================================

if uploaded_file is not None:

    # ====================================
    # SAVE FILE
    # ====================================

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        "Resume uploaded successfully."
    )

    # ====================================
    # EXTRACT TEXT
    # ====================================

    resume_text = extract_text_from_pdf(
        file_path
    )

    # ====================================
    # SKILL EXTRACTION
    # ====================================

    detected_skills = extract_skills(
        resume_text
    )

    # ====================================
    # ATS SCORE
    # ====================================

    ats_score, feedback = calculate_ats_score(
        resume_text,
        detected_skills
    )

    # ====================================
    # CAREER PREDICTION
    # ====================================

    transformed_resume = vectorizer.transform(
        [resume_text]
    )

    predicted_category = model.predict(
        transformed_resume
    )[0]

    # ====================================
    # METRICS
    # ====================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            label="ATS Score",
            value=f"{ats_score}/100"
        )

    with col2:

        st.metric(
            label="Skills Detected",
            value=len(detected_skills)
        )

    with col3:

        st.metric(
            label="Career Domain",
            value=predicted_category
        )

    st.markdown("---")

    # ====================================
    # TABS
    # ====================================

    tab1, tab2, tab3, tab4 = st.tabs([

        "Resume Analysis",

        "Detected Skills",

        "Job Recommendations",

        "Skill Gap Analysis"
    ])

    # ====================================
    # TAB 1
    # ====================================

    with tab1:

        st.markdown(
            '<div class="section-header">Extracted Resume Text</div>',
            unsafe_allow_html=True
        )

        st.text_area(
            "Resume Content",
            resume_text,
            height=350
        )

        st.markdown(
            '<div class="section-header">ATS Feedback</div>',
            unsafe_allow_html=True
        )

        if feedback:

            for item in feedback:

                st.warning(item)

        else:

            st.success(
                "Resume quality is good."
            )

    # ====================================
    # TAB 2
    # ====================================

    with tab2:

        st.markdown(
            '<div class="section-header">Detected Technical Skills</div>',
            unsafe_allow_html=True
        )

        if detected_skills:

            cols = st.columns(4)

            for i, skill in enumerate(
                detected_skills
            ):

                with cols[i % 4]:

                    st.markdown(
                        f"""
                        <div class="skill-box">
                            {skill}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        else:

            st.warning(
                "No skills detected."
            )

    # ====================================
    # TAB 3
    # ====================================

    with tab3:

        st.markdown(
            '<div class="section-header">Recommended Jobs</div>',
            unsafe_allow_html=True
        )

        recommended_jobs = semantic_job_search(
            resume_text
        )

        if recommended_jobs:

            # ====================================
            # VISUALIZATION
            # ====================================

            chart = plot_job_matches(
                recommended_jobs
            )

            st.pyplot(chart)

            st.markdown("---")

            # ====================================
            # JOB CARDS
            # ====================================

            for job in recommended_jobs:

                st.markdown(
                    '<div class="job-card">',
                    unsafe_allow_html=True
                )

                st.write(
                    f"### {job['title']}"
                )

                st.write(
                    f"Company: {job['company']}"
                )

                st.write(
                    f"Location: {job['location']}"
                )

                st.write(
                    f"Salary: {job['salary']}"
                )

                st.progress(
                    min(
                        int(job['match']),
                        100
                    )
                )

                st.write(
                    f"Match Score: {job['match']}%"
                )

                # ====================================
                # EXPLAINABLE AI
                # ====================================

                matched_skills = explain_recommendation(

                    detected_skills,

                    job["title"]
                )

                if matched_skills:

                    st.write(
                        "Matching Skills:"
                    )

                    for skill in matched_skills[:10]:

                        st.write(
                            f"- {skill}"
                        )

                else:

                    st.write(
                        "No strong matching skills detected."
                    )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

        else:

            st.warning(
                "No matching jobs found."
            )

    # ====================================
    # TAB 4
    # ====================================

    with tab4:

        st.markdown(
            '<div class="section-header">Skill Gap Analysis</div>',
            unsafe_allow_html=True
        )

        missing_skills = analyze_skill_gap(
            detected_skills,
            recommended_jobs
        )

        if missing_skills:

            st.write(
                "Recommended skills to improve:"
            )

            cols = st.columns(4)

            for i, skill in enumerate(
                missing_skills[:20]
            ):

                with cols[i % 4]:

                    st.error(skill)

        else:

            st.success(
                "Your resume already matches the required skills."
            )