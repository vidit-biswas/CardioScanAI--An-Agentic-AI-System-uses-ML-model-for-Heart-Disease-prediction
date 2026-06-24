from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_medical_research(query):

    results = client.search(
        query=query,
        max_results=5
    )

    return results