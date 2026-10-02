from utils.pdf_parser import extract_text_from_pdf


pdf_path = "uploads/resume1.pdf"

text = extract_text_from_pdf(pdf_path)

if text:
    print("\n========== EXTRACTED RESUME TEXT ==========\n")
    print(text)
    print("\n============================================")
else:
    print("No text could be extracted from the PDF.")