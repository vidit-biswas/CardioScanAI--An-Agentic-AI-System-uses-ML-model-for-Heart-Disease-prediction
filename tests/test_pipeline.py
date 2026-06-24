import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app.services.prediction_pipeline import predict_from_pdf

result = predict_from_pdf(
    "data/reports/sample_report.pdf"
)

print(result)