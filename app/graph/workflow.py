from langgraph.graph import StateGraph
from langgraph.graph import END

from app.graph.state import CardioState
from app.graph.nodes import *

builder = StateGraph(CardioState)

# Nodes

builder.add_node("pdf", pdf_node)
builder.add_node("extract", extraction_node)
builder.add_node("predict", prediction_node)
builder.add_node("explain", explanation_node)

builder.add_node("hitl", hitl_node)

builder.add_node("diet", diet_node)
builder.add_node("exercise", exercise_node)
builder.add_node("risk", risk_node)
builder.add_node("rag", rag_node)
builder.add_node("research", research_node)

builder.add_node("report", report_node)

# Entry Point

builder.set_entry_point("pdf")

# Main Pipeline

builder.add_edge("pdf", "extract")
builder.add_edge("extract", "predict")
builder.add_edge("predict", "explain")
builder.add_edge("explain", "hitl")

# HITL Router

builder.add_conditional_edges(
    "hitl",
    route_user,
    {
        "diet": "diet",
        "exercise": "exercise",
        "risk": "risk",
        "rag": "rag",
        "research": "research"
    }
)

# Every path goes to report

builder.add_edge("diet", "report")
builder.add_edge("exercise", "report")
builder.add_edge("risk", "report")
builder.add_edge("rag", "report")
builder.add_edge("research", "report")

# Report -> End

builder.add_edge("report", END)

# Finish Point

builder.set_finish_point("report")

graph = builder.compile()