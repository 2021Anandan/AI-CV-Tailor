from src.llm.models import generate
from src.llm.prompts import cover_letter_prompt

def generate_cover_letter(resume_text: str, job_description: str) -> str:
    prompt = cover_letter_prompt(resume_text, job_description)
    return generate(prompt)