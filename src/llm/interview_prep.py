from src.llm.models import generate
from src.llm.prompts import interview_prompt

def generate_interview_questions(resume_text: str, job_description: str) -> str:
    prompt = interview_prompt(resume_text, job_description)
    return generate(prompt)