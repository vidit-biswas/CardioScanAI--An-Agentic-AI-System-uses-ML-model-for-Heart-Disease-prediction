import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app.rag.retriever import retrieve_context

result = retrieve_context(
    "How can I lower cholesterol?"
)

print(result)