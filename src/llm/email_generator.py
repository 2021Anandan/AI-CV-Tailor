from src.llm.models import generate
from src.llm.prompts import email_prompt

def generate_cold_email(resume_text: str, job_description: str) -> str:
    prompt = email_prompt(resume_text, job_description)
    return generate(prompt)