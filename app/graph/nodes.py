from app.pdf_processing.pdf_parsing import extract_text_from_pdf
from app.llm.extractor import extract_medical_parameters
from app.predictor import predict_heart_disease
from app.llm.explainer import explain_prediction

from app.rag.generator import answer_question

from app.research.research_agent import run_research_agent

from app.reports.report_generator import generate_report

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# PDF NODE

def pdf_node(state):

    text = extract_text_from_pdf(
        state["pdf_path"]
    )

    return {
        "report_text": text
    }


# EXTRACTION NODE

def extraction_node(state):

    patient_data = extract_medical_parameters(
        state["report_text"]
    )

    return {
        "patient_data": patient_data
    }

#PREDICTION NODE

def prediction_node(state):

    prediction = predict_heart_disease(
        state["patient_data"]
    )

    return {
        "prediction_result": prediction
    }


# EXPLANATION NODE

def explanation_node(state):

    explanation = explain_prediction(
        state["patient_data"],
        state["prediction_result"]
    )

    return {
        "explanation": explanation
    }


# =====================================================
# HITL NODE
# =====================================================

def hitl_node(state):

    print("\n===== HUMAN IN THE LOOP =====")

    print("1. Diet Plan")
    print("2. Exercise Plan")
    print("3. Risk Factors")
    print("4. Ask Question")
    print("5. Latest Research")

    choice = input(
        "\nChoose option: "
    )

    result = {
        "user_choice": choice
    }

    if choice == "4":

        question = input(
            "\nEnter Question: "
        )

        result["user_question"] = question

    return result


# ROUTER


def route_user(state):

    choice = state["user_choice"]

    if choice == "1":
        return "diet"

    elif choice == "2":
        return "exercise"

    elif choice == "3":
        return "risk"

    elif choice == "5":
        return "research"

    else:
        return "rag"



# RAG NODE WITH MEMORy

def rag_node(state):

    history = state.get(
        "chat_history",
        []
    )

    answer = answer_question(
        question=state["user_question"],
        patient_data=state["patient_data"],
        prediction_result=state["prediction_result"],
        chat_history=history
    )

    history.append(
        {
            "question": state["user_question"],
            "answer": answer
        }
    )

    print("\n===== RAG RESPONSE =====\n")
    print(answer)

    return {
        "final_response": answer,
        "chat_history": history
    }

# DIET NODE


def diet_node(state):

    prompt = f"""
Create a personalized heart healthy diet plan.

Patient Data:

{state['patient_data']}

Prediction:

{state['prediction_result']}

Give:

- Foods to eat
- Foods to avoid
- Weekly recommendations
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "final_response":
        response.choices[0].message.content
    }



# EXERCISE NODE


def exercise_node(state):

    prompt = f"""
Create a heart healthy exercise plan.

Patient:

{state['patient_data']}

Prediction:

{state['prediction_result']}

Give:

- Safe exercises
- Weekly schedule
- Precautions
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "final_response":
        response.choices[0].message.content
    }



# RISK FACTOR NODE


def risk_node(state):

    prompt = f"""
Explain major risk factors.

Patient:

{state['patient_data']}

Prediction:

{state['prediction_result']}

Use bullet points.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "final_response":
        response.choices[0].message.content
    }



# RESEARCH NODE


def research_node(state):

    query = input(
        "\nResearch Topic: "
    )

    result = run_research_agent(
        query=query,
        patient_data=state["patient_data"],
        prediction_result=state["prediction_result"]
    )

    print("\n===== RESEARCH RESPONSE =====\n")
    print(result)

    return {
        "final_response": result
    }



# REPORT NODE


def report_node(state):

    report_path = generate_report(
        patient_data=state["patient_data"],
        prediction_result=state["prediction_result"],
        explanation=state["explanation"],
        final_response=state["final_response"]
    )

    print("\nPDF CREATED:\n")
    print(report_path)

    return {
        "report_path": report_path
    }