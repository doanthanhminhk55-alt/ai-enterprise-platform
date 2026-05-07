from fastapi import APIRouter

from app.rag.rag_pipeline import retrieve_context
from app.rag.groq_service import ask_groq

router = APIRouter()

@router.get("/chat")

def chat(question: str):

    context = retrieve_context(question)

    answer = ask_groq(
        context=context,
        question=question
    )

    return {
        "question": question,
        "answer": answer
    }