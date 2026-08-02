from pathlib import Path

from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.docx_parser import extract_text_from_docx
from src.parser.exceptions import (
    UnsupportedFileTypeError,
    EmptyResumeError,
)


def extract_resume_text(uploaded_file):
    """
    Extract text from a supported resume file.
    """

    suffix = Path(uploaded_file.name).suffix.lower()

    if suffix == ".pdf":
        text = extract_text_from_pdf(uploaded_file)

    elif suffix == ".docx":
        text = extract_text_from_docx(uploaded_file)

    else:
        raise UnsupportedFileTypeError(
            f"Unsupported file type: {suffix}"
        )

    if not text.strip():
        raise EmptyResumeError("Resume contains no readable text.")

    return text