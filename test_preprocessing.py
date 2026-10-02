from utils.pdf_parser import extract_text_from_pdf
from utils.text_processor import preprocess_text


pdf_path = "uploads/resume1.pdf"

# Extract text
raw_text = extract_text_from_pdf(pdf_path)

print("\n========== RAW TEXT ==========\n")
print(raw_text)


# Preprocess text
cleaned_text = preprocess_text(raw_text)

print("\n========== CLEANED TEXT ==========\n")
print(cleaned_text)