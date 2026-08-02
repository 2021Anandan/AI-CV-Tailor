import os
from google import genai

def get_gemini_client() -> genai.Client:
    """
    Initializes and returns a centralized Google GenAI client instance.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    return genai.Client(api_key=api_key) if api_key else genai.Client()

def call_gemini_model(prompt: str, model_name: str = "gemini-3.5-flash") -> str:
    """
    Centralized execution function with error handling for Gemini model calls.
    """
    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"AI generation failed: {e}"

def generate(prompt: str, provider: str = "gemini", model_name: str = "gemini-3.5-flash") -> str:
    """
    Provider abstraction interface to support swapping between LLM providers easily.
    """
    if provider.lower() == "gemini":
        return call_gemini_model(prompt, model_name=model_name)
    # Future providers (e.g., Ollama, OpenAI) can be easily added here
    raise ValueError(f"Unsupported LLM provider: {provider}")