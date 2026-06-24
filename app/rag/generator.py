import os

from dotenv import load_dotenv
from groq import Groq

from app.rag.retriever import retrieve_context

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def answer_question(
    question,
    patient_data,
    prediction_result,
    chat_history=None
):
    context = retrieve_context(question)

    prompt = f"""
You are a heart disease assistant.

Patient Information:
  {patient_data}

Prediction Result:
{prediction_result}

Previous Conversation:
{chat_history}

Knowledge Base Context:
{context}

User Question:
{question}

Instructions:
- Use patient data.
- Use previous conversation.
- Use retrieved context.
- Answer in bullet points.
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