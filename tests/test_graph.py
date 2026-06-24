import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app.graph.workflow import graph

result = graph.invoke(
    {
        "pdf_path": "data/reports/sample_report.pdf",
        "user_question": "What foods should I avoid?"
    }
)

print("\nFINAL RESPONSE:\n")

print(result.get("final_response"))