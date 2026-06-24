import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def explain_prediction(patient_data, prediction_result):

    prompt = f"""
You are a medical AI assistant.

Patient Data:
{patient_data}

Prediction:
{prediction_result}

Explain:

1. Risk Level
2. Important Factors
3. Precautions
4. Lifestyle Suggestions

Use bullet points.
Keep it simple.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content 