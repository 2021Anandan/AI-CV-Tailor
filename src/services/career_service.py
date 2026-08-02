from src.parser.extractor import extract_resume_text
from src.ats.scorer import calculate_ats_score
from src.llm.optimizer import optimize_resume
from src.llm.cover_letter import generate_cover_letter
from src.llm.email_generator import generate_cold_email
from src.llm.interview_prep import generate_interview_questions

class CareerService:
    def parse_resume(self, uploaded_file):
        return extract_resume_text(uploaded_file)

    def evaluate_ats(self, resume_text, job_desc):
        return calculate_ats_score(resume_text, job_desc)

    def optimize_resume(self, resume_text, job_desc):
        return optimize_resume(resume_text, job_desc)

    def generate_cover_letter(self, resume_text, job_desc):
        return generate_cover_letter(resume_text, job_desc)

    def generate_recruiter_email(self, resume_text, job_desc):
        return generate_cold_email(resume_text, job_desc)

    def generate_interview_guide(self, resume_text, job_desc):
        return generate_interview_questions(resume_text, job_desc)

    def analyze_resume(self, uploaded_file, job_description):
        resume_text = self.parse_resume(uploaded_file)
        ats = self.evaluate_ats(resume_text, job_description)
        optimized = self.optimize_resume(resume_text, job_description)
        cover_letter = self.generate_cover_letter(resume_text, job_description)
        cold_email = self.generate_recruiter_email(resume_text, job_description)
        interview_questions = self.generate_interview_guide(resume_text, job_description)

        return {
            "resume_text": resume_text,
            "ats": ats,
            "optimized_resume": optimized,
            "cover_letter": cover_letter,
            "cold_email": cold_email,
            "interview_questions": interview_questions,
        }