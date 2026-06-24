
from app.research.search import search_medical_research
from app.research.summarizer import summarize_research

def run_research_agent(
    query,
    patient_data,
    prediction_result
):

    raw = search_medical_research(query)

    articles = ""

    for item in raw["results"]:

        articles += f"""
    Title: {item['title']}

    Content: {item['content']}

    Source: {item['url']}
    --------------------
    """
    summary = summarize_research(
        articles,
        patient_data,
        prediction_result
    )

    return summary