from fastapi import APIRouter
from app.agents.graph import graph
from app.memory.chat_memory import (
    add_message,
    get_messages
)

router = APIRouter()

@router.get("/chat")

def chat(
    question: str,
    session_id: str = "default"
):
    add_message(
        session_id,
        "user",
        question
    )

    result = graph.invoke({
        "question": question
    })

    answer = result["answer"]

    add_message(
        session_id,
        "assistant",
        answer
    )

    return {
        "question": question,
        "answer": answer,
        "memory": get_messages(session_id)
    }

    