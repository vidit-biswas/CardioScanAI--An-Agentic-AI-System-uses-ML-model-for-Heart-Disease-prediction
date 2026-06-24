from typing import TypedDict


class CardioState(TypedDict, total=False):

    pdf_path: str

    report_text: str

    patient_data: dict

    prediction_result: dict

    explanation: str

    user_choice: str

    user_question: str

    final_response: str

    report_path: str

    chat_history: list