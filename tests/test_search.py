import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
from app.research.search import search_medical_research

results = search_medical_research(
    "Latest cholesterol treatment research"
)

print(results)