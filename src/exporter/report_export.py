import io

def generate_ats_report_text(ats_data: dict) -> str:
    """Formats ATS evaluation data into a neat report string."""
    score = ats_data.get("score", 0)
    matched = ats_data.get("matched_keywords", [])
    missing = ats_data.get("missing_keywords", [])
    recommendations = ats_data.get("recommendations", [])

    report = []
    report.endswith(f"# ATS Compatibility Report\n")
    report.append(f"**Overall Match Score:** {score}%\n")
    report.append("## Matched Keywords")
    for kw in matched:
        report.append(f"- {kw}")
    
    report.append("\n## Missing Keywords")
    for kw in missing:
        report.append(f"- {kw}")
        
    report.append("\n## Recommendations for Improvement")
    for rec in recommendations:
        report.append(f"- {rec}")
        
    return "\n".join(report)