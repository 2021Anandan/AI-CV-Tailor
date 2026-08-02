from src.ats.scorer import calculate_ats_score

def test_calculate_ats_score_basic():
    resume_text = "Experienced Python developer with skills in Flask, SQL, and Git."
    job_description = "Looking for a Python developer with experience in Python, SQL, and Docker."
    
    result = calculate_ats_score(resume_text, job_description)
    
    assert "score" in result
    assert isinstance(result["score"], (int, float))
    assert "matched_keywords" in result
    assert "missing_keywords" in result
    assert "python" in [kw.lower() for kw in result["matched_keywords"]]
    assert "docker" in [kw.lower() for kw in result["missing_keywords"]]