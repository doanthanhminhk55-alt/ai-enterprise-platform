from app.rag.pdf_loader import extract_text_from_pdf
from app.rag.chunker import chunk_text
from app.rag.embedding import create_embedding

from app.rag.chroma_service import (
    store_chunks,
    search_similar
)

def process_pdf(file_path):

    text = extract_text_from_pdf(file_path)

    chunks = chunk_text(text)

    embeddings = []

    for chunk in chunks:

        embedding = create_embedding(chunk)

        embeddings.append(embedding)

    store_chunks(
        chunks=chunks,
        embeddings=embeddings
    )

def retrieve_context(question):

    query_embedding = create_embedding(question)

    results = search_similar(query_embedding)

    documents = results["documents"][0]

    context = "\n".join(documents)

    return context