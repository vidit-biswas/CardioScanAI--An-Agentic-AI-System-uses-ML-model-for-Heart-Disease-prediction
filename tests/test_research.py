import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
from app.research.research_agent import run_research_agent

result = run_research_agent(
    query="Latest cholesterol treatment research",
    patient_data={
        "Age":58,
        "Cholesterol":265
    },
    prediction_result={
        "prediction":1,
        "risk_score":94.27
    }
)

print(result)