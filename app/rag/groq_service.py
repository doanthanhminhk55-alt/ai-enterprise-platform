from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_groq(context, question):

    prompt = f"""
You are an AI assistant.

Answer ONLY from context.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def ask_groq_stream(context, question):

    prompt = f"""
Context:
{context}

Question:
{question}
"""

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        stream=True
    )

    for chunk in stream:

        content = chunk.choices[0].delta.content

        if content:
            yield content