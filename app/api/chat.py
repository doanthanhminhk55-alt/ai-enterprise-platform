from fastapi import APIRouter

from app.agents.graph import graph

from app.memory.memory_manager import (
    add_to_memory
)

router = APIRouter()

@router.get("/chat")

def chat(
    question: str,
    session_id: str = "default"
):

    result = graph.invoke({

        "session_id": session_id,

        "question": question,

        "memory": "",

        "plan": "",

        "context": "",

        "research": "",

        "critique": "",

        "answer": ""
    })

    answer = result["answer"]

    add_to_memory(
        session_id,
        "user",
        question
    )

    add_to_memory(
        session_id,
        "assistant",
        answer
    )

    return result