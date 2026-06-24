import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app.rag.generator import answer_question

response = answer_question(
    "How can I reduce cholesterol?"
)

print(response)