from docx import Document


def extract_text_from_docx(uploaded_file):
    """
    Extract text from a DOCX resume.
    """

    text = ""

    document = Document(uploaded_file)

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text.strip()