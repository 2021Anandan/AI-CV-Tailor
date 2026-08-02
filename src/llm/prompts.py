def resume_prompt(resume_text: str, job_description: str) -> str:
    return f"""
    You are an expert resume writer and ATS optimization specialist. Rewrite and optimize the following resume to better match the target job description. Ensure it highlights relevant skills, uses strong action verbs, and is optimized for ATS parsing without losing authenticity.
    
    Target Job Description:
    {job_description}
    
    Original Resume:
    {resume_text}
    
    Optimized Resume:
    """

def cover_letter_prompt(resume_text: str, job_description: str) -> str:
    return f"""
    You are an expert career consultant. Write a professional, compelling cover letter based on the following candidate resume and target job description.
    
    Target Job Description:
    {job_description}
    
    Candidate Resume:
    {resume_text}
    
    Cover Letter:
    """

def email_prompt(resume_text: str, job_description: str) -> str:
    return f"""
    You are an expert career consultant. Write a professional, compelling cold outreach email to a recruiter or hiring manager based on the following resume and target job description.
    
    Target Job Description:
    {job_description}
    
    Candidate Resume:
    {resume_text}
    
    Cold Email:
    """

def interview_prompt(resume_text: str, job_description: str) -> str:
    return f"""
    You are an expert technical interviewer and career coach. Based on the following candidate resume and target job description, generate a comprehensive set of interview preparation materials containing:
    1. Technical questions specific to the job requirements.
    2. Behavioral and HR questions.
    3. Sample high-scoring answers or key talking points for each.
    
    Target Job Description:
    {job_description}
    
    Candidate Resume:
    {resume_text}
    
    Interview Preparation Guide:
    """