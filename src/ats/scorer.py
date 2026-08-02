"""
ATS Scoring Engine
"""

def calculate_ats_score(resume_text: str, job_description: str):
    """
    Basic ATS scoring based on keyword matching.
    """

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    matched = resume_words.intersection(jd_words)
    missing = jd_words - resume_words

    if len(jd_words) == 0:
        score = 0
    else:
        score = int((len(matched) / len(jd_words)) * 100)

    return {
        "score": score,
        "matched_keywords": sorted(list(matched)),
        "missing_keywords": sorted(list(missing))
    }