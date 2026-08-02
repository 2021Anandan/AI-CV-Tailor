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
    from src.llm.optimizer import generate_optimized_resume
from src.llm.cover_letter import generate_cover_letter
from src.llm.email_generator import generate_cold_email
from src.llm.interview_prep import generate_interview_questions

# --------------------------------------------------
# AI Generation Modules
# --------------------------------------------------
st.markdown("---")
st.markdown("## 🤖 AI Advanced Modules")

tab1, tab2, tab3, tab4 = st.tabs([
    "✨ Resume Optimization", 
    "📝 Cover Letter", 
    "📧 Cold Email", 
    "🎯 Interview Prep"
])

with tab1:
    st.subheader("AI Resume Optimization")
    if st.button("Generate Optimized Resume"):
        with st.spinner("Optimizing resume for target job..."):
            optimized_cv = generate_optimized_resume(resume_text, job_description)
            st.text_area("Optimized Content", optimized_cv, height=300)

with tab2:
    st.subheader("Cover Letter Generator")
    if st.button("Generate Cover Letter"):
        with st.spinner("Drafting professional cover letter..."):
            cover_letter = generate_cover_letter(resume_text, job_description)
            st.text_area("Cover Letter", cover_letter, height=300)

with tab3:
    st.subheader("Email Generator")
    if st.button("Generate Cold Email"):
        with st.spinner("Drafting recruiter outreach email..."):
            cold_email = generate_cold_email(resume_text, job_description)
            st.text_area("Cold Email", cold_email, height=300)

with tab4:
    st.subheader("Interview Preparation")
    if st.button("Generate Interview Questions"):
        with st.spinner("Preparing tailored technical & HR questions..."):
            questions = generate_interview_questions(resume_text, job_description)
            st.markdown(questions)