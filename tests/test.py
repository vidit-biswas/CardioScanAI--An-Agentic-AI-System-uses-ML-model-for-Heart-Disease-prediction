import sys
import os

sys.path.append(os.path.abspath("."))

from app.pdf_processing.pdf_parsing import extract_text_from_pdf

text = extract_text_from_pdf("data/reports/sample_report.pdf")

print(text)