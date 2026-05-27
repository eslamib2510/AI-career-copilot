import re

# ====================================
# ATS SCORING SYSTEM
# ====================================

def calculate_ats_score(
    text,
    skills
):

    score = 0

    feedback = []

    text_lower = text.lower()

    # ====================================
    # SKILLS SCORE
    # ====================================

    skills_count = len(skills)

    skills_score = min(
        skills_count * 4,
        40
    )

    score += skills_score

    # ====================================
    # EDUCATION
    # ====================================

    if "education" in text_lower:

        score += 15

    else:

        feedback.append(
            "Add an Education section."
        )

    # ====================================
    # EXPERIENCE
    # ====================================

    if "experience" in text_lower:

        score += 20

    else:

        feedback.append(
            "Add an Experience section."
        )

    # ====================================
    # PROJECTS
    # ====================================

    if "project" in text_lower:

        score += 15

    else:

        feedback.append(
            "Add a Projects section."
        )

    # ====================================
    # CERTIFICATIONS
    # ====================================

    certification_keywords = [

        "certificate",
        "certification",
        "aws",
        "google",
        "coursera"
    ]

    cert_found = any(

        keyword in text_lower

        for keyword in certification_keywords
    )

    if cert_found:

        score += 10

    else:

        feedback.append(
            "Add certifications to strengthen the resume."
        )

    # ====================================
    # WORD COUNT
    # ====================================

    words = re.findall(
        r"\w+",
        text
    )

    word_count = len(words)

    if word_count >= 300:

        score += 10

    else:

        feedback.append(
            "Resume content is too short."
        )

    # ====================================
    # FINAL LIMIT
    # ====================================

    score = min(score, 100)

    return score, feedback