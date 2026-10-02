from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract text from all pages of a PDF resume.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """

    try:
        reader = PdfReader(pdf_path)

        extracted_text = ""

        for page in reader.pages:
            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

        return extracted_text.strip()

    except Exception as e:
        print(f"Error while reading PDF: {e}")
        return ""