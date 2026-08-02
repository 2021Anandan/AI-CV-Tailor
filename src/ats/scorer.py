"""
ATS Scoring Engine
AI CV Tailor

Version: 2.0
"""

import re

# Common words that should not influence ATS scoring
STOP_WORDS = {
    "the", "and", "or", "for", "to", "of", "in", "on", "with",
    "a", "an", "is", "are", "be", "as", "at", "by", "from",
    "this", "that", "these", "those", "your", "our", "their",
    "will", "can", "should", "must", "have", "has", "had"
}


def tokenize(text: str) -> set:
    """
    Convert text into a cleaned set of keywords.
    """

    words = re.findall(r"\b[a-zA-Z][a-zA-Z0-9+#.-]*\b", text.lower())

    return {
        word
        for word in words
        if word not in STOP_WORDS and len(word) > 1
    }


def calculate_ats_score(resume_text: str, job_description: str):
    """
    Calculate ATS compatibility score.
    """

    resume_keywords = tokenize(resume_text)
    jd_keywords = tokenize(job_description)

    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords - resume_keywords

    score = 0

    if jd_keywords:
        score = round((len(matched) / len(jd_keywords)) * 100)

    suggestions = []

    if missing:
        suggestions.append(
            "Include more relevant keywords from the Job Description."
        )

    if score < 60:
        suggestions.append(
            "Resume needs significant ATS optimization."
        )
    elif score < 80:
        suggestions.append(
            "Resume is fairly optimized but can be improved."
        )
    else:
        suggestions.append(
            "Resume is well optimized for ATS."
        )

    return {
        "score": score,
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "matched_count": len(matched),
        "missing_count": len(missing),
        "total_keywords": len(jd_keywords),
        "suggestions": suggestions,
    }