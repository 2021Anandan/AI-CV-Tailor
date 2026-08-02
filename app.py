import streamlit as st
from pathlib import Path
from src.parser.docx_parser import extract_text_from_docx
from src.parser.pdf_parser import extract_text_from_pdf
from src.ats.scorer import calculate_ats_score

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI CV Tailor",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("📄 AI CV Tailor")
st.subheader("Tailor your Resume for Any Job using AI")

st.markdown("---")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("About")
st.sidebar.markdown("---")

st.sidebar.subheader("Developer")
st.sidebar.markdown("### Anandan M A")
st.sidebar.markdown("**Founder**")
st.sidebar.markdown("**RTVMS Innovations**")

st.sidebar.info("""
AI CV Tailor

✔ Resume Parser
✔ ATS Score
✔ Resume Optimization
✔ Cover Letter Generator
✔ Email Generator
✔ Interview Preparation
""")

# --------------------------------------------------
# Main Layout
# --------------------------------------------------
left, right = st.columns(2)

with left:
    st.header("Upload Resume")

    resume = st.file_uploader(
        "Choose Resume",
        type=["pdf", "docx"]
    )

with right:
    st.header("Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=300,
        placeholder="Paste the complete Job Description here..."
    )

st.markdown("---")

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------
if st.button("🚀 Analyze Resume", use_container_width=True):

    # Validation
    if resume is None:
        st.error("Please upload a Resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please paste the Job Description.")
        st.stop()

    st.success("Inputs received successfully!")

    # --------------------------------------------------
    # Resume Information
    # --------------------------------------------------
    st.markdown("## Resume Information")

    st.write(f"**Filename:** {resume.name}")
    st.write(f"**File Size:** {round(resume.size / 1024, 2)} KB")
    st.write(f"**File Type:** {Path(resume.name).suffix}")

    # --------------------------------------------------
    # Resume Parsing & ATS Scoring
    # --------------------------------------------------
    if Path(resume.name).suffix.lower() == ".pdf":

        resume_text = extract_text_from_pdf(resume)
        ats_result = calculate_ats_score(resume_text, job_description)
        st.success("✅ PDF Resume parsed successfully!")

        st.text_area(
            "Extracted Resume",
            resume_text,
            height=300
        )

        # ATS Score Display inside the button logic
        st.markdown("## ATS Score")
        st.metric(
            "Overall ATS Score",
            f"{ats_result['score']}%"
        )
        st.markdown("### Matched Keywords")
        st.write(", ".join(ats_result["matched_keywords"]))

    elif Path(resume.name).suffix.lower() == ".docx":

        resume_text = extract_text_from_docx(resume)
        ats_result = calculate_ats_score(resume_text, job_description)
        st.success("✅ DOCX Resume parsed successfully!")

        st.text_area(
            "Extracted Resume",
            resume_text,
            height=300
        )

        # ATS Score Display inside the button logic
        st.markdown("## ATS Score")
        st.metric(
            "Overall ATS Score",
            f"{ats_result['score']}%"
        )
        st.markdown("### Matched Keywords")
        st.write(", ".join(ats_result["matched_keywords"]))

    # --------------------------------------------------
    # Job Description Summary
    # --------------------------------------------------
    st.markdown("## Job Description")

    st.write(f"Characters: {len(job_description)}")
    st.write(f"Words: {len(job_description.split())}")