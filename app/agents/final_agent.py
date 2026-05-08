from app.rag.groq_service import ask_groq

def final_agent(
    question,
    context,
    research,
    critique
):

    prompt = f"""
Generate the final improved answer.

Question:
{question}

Context:
{context}

Research:
{research}

Critique:
{critique}

Provide:
- accurate answer
- concise explanation
- final polished response
"""

    answer = ask_groq(
        context=context,
        question=prompt
    )

    return answer