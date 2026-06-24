from app.pdf_processing.pdf_parsing import extract_text_from_pdf
from app.llm.extractor import extract_medical_parameters
from app.llm.explainer import explain_prediction
from app.predictor import predict_heart_disease


def predict_from_pdf(pdf_path):

    report_text = extract_text_from_pdf(pdf_path)

    patient_data = extract_medical_parameters(
        report_text
    )

    prediction = predict_heart_disease(
        patient_data
    )

    explanation = explain_prediction(
        patient_data,
        prediction
    )

    return {
        "patient_data": patient_data,
        "prediction_result": prediction,
        "explanation": explanation
    }