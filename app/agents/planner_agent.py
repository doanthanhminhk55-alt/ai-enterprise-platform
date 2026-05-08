from app.rag.groq_service import ask_groq

def planner_agent(question: str):

    prompt = f"""
You are a planning AI agent.

Break the user's question into a plan.

Question:
{question}
"""

    plan = ask_groq(
        context="",
        question=prompt
    )

    return plan