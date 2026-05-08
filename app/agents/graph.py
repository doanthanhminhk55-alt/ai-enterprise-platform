from langgraph.graph import StateGraph, END

from app.agents.state import AgentState
from app.agents.tools import retrieve_tool

from app.rag.groq_service import ask_groq

def retrieve_node(state: AgentState):

    question = state["question"]

    context = retrieve_tool(question)

    return {
        "context": context
    }

def answer_node(state: AgentState):

    answer = ask_groq(
        context=state["context"],
        question=state["question"]
    )

    return {
        "answer": answer
    }

workflow = StateGraph(AgentState)

workflow.add_node(
    "retrieve",
    retrieve_node
)

workflow.add_node(
    "answer",
    answer_node
)

workflow.set_entry_point("retrieve")

workflow.add_edge(
    "retrieve",
    "answer"
)

workflow.add_edge(
    "answer",
    END
)

graph = workflow.compile()