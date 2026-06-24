import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def extract_medical_parameters(report_text):

    prompt = f"""
You are a medical data extraction system.

Return ONLY valid JSON.

Do not explain.
Do not use markdown.
Do not add extra text.

Schema:

{{
  "Age": int,
  "Sex": str,
  "ChestPainType": str,
  "RestingBP": int,
  "Cholesterol": int,
  "FastingBS": int,
  "RestingECG": str,
  "MaxHR": int,
  "ExerciseAngina": str,
  "Oldpeak": float,
  "ST_Slope": str
}}

Medical Report:

{report_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )



    result = response.choices[0].message.content

    print("\n===== LLM RESPONSE =====")
    print(result)
    print("========================\n")

    return json.loads(result)