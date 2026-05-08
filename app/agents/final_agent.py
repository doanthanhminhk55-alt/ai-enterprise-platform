from app.rag.groq_service import ask_groq

def final_agent(
    question,
    memory,
    context,
    research,
    critique
):

    prompt = f"""
You are a powerful AI assistant.

Conversation Memory:
{memory}

Retrieved Context:
{context}

Research:
{research}

Critique:
{critique}

Question:
{question}

Generate the best final answer.
"""

    answer = ask_groq(
        context=context,
        question=prompt
    )

    return answer