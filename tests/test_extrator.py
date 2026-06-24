import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app.pdf_processing.pdf_parsing import extract_text_from_pdf
from app.llm.extractor import extract_medical_parameters

text = extract_text_from_pdf(
    "data/reports/sample_report.pdf"
)

result = extract_medical_parameters(text)

print(result)