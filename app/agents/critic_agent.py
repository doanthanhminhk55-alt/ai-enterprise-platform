from app.rag.groq_service import ask_groq

def critic_agent(question, research):

    prompt = f"""
You are a critic AI agent.

Review the answer carefully.

Find:
- hallucinations
- missing facts
- weak reasoning

Question:
{question}

Research:
{research}
"""

    critique = ask_groq(
        context=research,
        question=prompt
    )

    return critique