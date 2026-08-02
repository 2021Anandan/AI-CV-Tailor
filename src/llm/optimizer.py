from src.llm.models import generate
from src.llm.prompts import resume_prompt

def optimize_resume(resume_text: str, job_description: str) -> str:
    prompt = resume_prompt(resume_text, job_description)
    return generate(prompt)