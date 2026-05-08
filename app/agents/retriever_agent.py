from app.rag.rag_pipeline import retrieve_context

def retriever_agent(question: str):

    context = retrieve_context(question)

    return context