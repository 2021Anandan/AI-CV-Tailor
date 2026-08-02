import streamlit as st
from pathlib import Path

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
st.sidebar.info(
    """
AI CV Tailor

✔ Resume Parser
✔ ATS Score
✔ Resume Optimization
✔ Cover Letter Generator
✔ Email Generator
✔ Interview Preparation
"""
)

# --------------------------------------------------
# Layout
# --------------------------------------------------
left, right = st.columns([1, 1])

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

    if resume is None:
        st.error("Please upload a Resume.")
        st.stop()

    if len(job_description.strip()) == 0:
        st.error("Please paste the Job Description.")
        st.stop()

    st.success("Inputs received successfully!")

    st.markdown("## Resume Information")

    st.write(f"**Filename:** {resume.name}")
    st.write(f"**File Size:** {round(resume.size/1024,2)} KB")
    st.write(f"**File Type:** {Path(resume.name).suffix}")

    st.markdown("## Job Description")

    st.write(f"Characters: {len(job_description)}")
    st.write(f"Words: {len(job_description.split())}")

    st.info("Resume parsing will be added in Version 0.3.0")