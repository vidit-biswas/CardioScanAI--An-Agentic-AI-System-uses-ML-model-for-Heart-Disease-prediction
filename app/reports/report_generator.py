from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

import os


def generate_report(
    patient_data,
    prediction_result,
    explanation,
    final_response,
    output_path="reports/final_report.pdf"
):

    os.makedirs("reports", exist_ok=True)

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "CardioScan AI Medical Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # Patient Data
   # Patient Data
    elements.append(
        Paragraph(
            "<b>Patient Information</b>",
             styles["Heading2"]
        )
    )

    patient_html = ""

    for key, value in patient_data.items():
        patient_html += f"<b>{key}:</b> {value}<br/>"

    elements.append(
        Paragraph(
            patient_html,
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1, 15))

    # Prediction Result
    elements.append(
        Paragraph(
            "<b>Prediction Result</b>",
            styles["Heading2"]
        )
    )

    prediction_html = f"""
    <b>Prediction:</b> {"Heart Disease Detected" if prediction_result["prediction"] == 1 else "No Heart Disease"}<br/>
    <b>Risk Score:</b> {prediction_result["risk_score"]}%<br/>
    """

    elements.append(
        Paragraph(
            prediction_html,
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1, 15))

    # Explanation
    elements.append(
        Paragraph(
            "<b>Risk Explanation</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            explanation.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    # Personalized Recommendation
    elements.append(
        Paragraph(
            "<b>Personalized Recommendation</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            final_response.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(elements)

    return output_path