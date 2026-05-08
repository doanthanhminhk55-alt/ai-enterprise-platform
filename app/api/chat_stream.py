from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.rag.rag_pipeline import retrieve_context
from app.rag.groq_service import ask_groq_stream

router = APIRouter()

@router.get("/chat-stream")

def chat_stream(question: str):

    context = retrieve_context(question)

    return StreamingResponse(
        ask_groq_stream(
            context,
            question
        ),
        media_type="text/plain"
    )