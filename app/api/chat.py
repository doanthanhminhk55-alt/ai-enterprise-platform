from fastapi import APIRouter

from app.agents.graph import graph

router = APIRouter()

@router.get("/chat")

def chat(question: str):

    result = graph.invoke({

        "question": question,

        "plan": "",

        "context": "",

        "research": "",

        "critique": "",

        "answer": ""
    })

    return result