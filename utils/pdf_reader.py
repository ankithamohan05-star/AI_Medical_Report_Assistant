import fitz


def extract_text_from_pdf(uploaded_file):
    """Extract text from an uploaded PDF."""

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text