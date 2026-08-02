import streamlit as st
from pathlib import Path
from src.services.career_service import CareerService
from src.exporter.docx_export import create_docx

st.set_page_config(page_title="AI CV Tailor", page_icon="📄", layout="wide")

st.title("📄 AI CV Tailor - Production Dashboard")
st.markdown("Transform your resume, beat ATS filters, and generate interview materials seamlessly.")

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Upload Resume (.pdf or .docx)", type=["pdf", "docx"])
    job_description = st.text_area("Paste Job Description Here", height=200)
    analyze_btn = st.button("🚀 Analyze & Tailor Resume", type="primary")

if analyze_btn:
    if not uploaded_file or not job_description:
        st.error("Please upload a resume and provide a job description.")
    else:
        with st.spinner("Processing through CareerService orchestration layer..."):
            try:
                service = CareerService()
                result = service.analyze_resume(uploaded_file, job_description)
                
                st.session_state["result"] = result
                st.success("Analysis completed successfully!")
            except Exception as e:
                st.error(f"Error during analysis: {e}")

if "result" in st.session_state:
    res = st.session_state["result"]
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 ATS Score", "✨ Optimized Resume", "✉️ Cover Letter & Email", "❓ Interview Guide", "📥 Export"])
    
    with tab1:
        st.subheader("ATS Compatibility Analysis")
        ats_data = res["ats"]
        st.metric(label="Overall ATS Score", value=f"{ats_data.get('score', 0)} / 100")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Matched Keywords:**")
            for kw in ats_data.get("matched_keywords", []):
                st.markdown(f"- ✅ {kw}")
        with col2:
            st.markdown("**Missing Keywords:**")
            for kw in ats_data.get("missing_keywords", []):
                st.markdown(f"- ❌ {kw}")
                
    with tab2:
        st.subheader("Tailored Resume Content")
        st.text_area("Optimized Output", res["optimized_resume"], height=300)
        
    with tab3:
        st.subheader("Generated Cover Letter & Recruiter Email")
        st.markdown("### Cover Letter")
        st.text_area("Cover Letter", res["cover_letter"], height=200)
        st.markdown("### Recruiter Cold Email")
        st.text_area("Cold Email", res["cold_email"], height=150)
        
    with tab4:
        st.subheader("Interview Preparation Guide")
        for idx, q in enumerate(res["interview_questions"], 1):
            st.markdown(f"**Q{idx}:** {q}")
            
    with tab5:
        st.subheader("Export Options")
        st.markdown("Download your customized artifacts.")
        docx_file = create_docx(res["optimized_resume"])
        st.download_button(
            label="Download Optimized Resume (DOCX)",
            data=docx_file,
            file_name="optimized_resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )