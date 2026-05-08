from app.rag.rag_pipeline import retrieve_context

def retrieve_tool(question: str):

    context = retrieve_context(question)

    return context