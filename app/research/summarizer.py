from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_research(
    articles,
    patient_data,
    prediction_result
):

    prompt = f"""
Patient Data:
{patient_data}

Prediction:
{prediction_result}

Research Articles:
{articles}

Summarize:

- Latest findings
- Important discoveries
- How it relates to this patient
- Actionable recommendations

Use bullet points.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content