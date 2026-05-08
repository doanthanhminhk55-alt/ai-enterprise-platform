from app.rag.groq_service import ask_groq

def researcher_agent(question, context):

    prompt = f"""
You are a research AI agent.

Analyze the retrieved context carefully.

Question:
{question}

Context:
{context}
"""

    research = ask_groq(
        context=context,
        question=prompt
    )

    return research