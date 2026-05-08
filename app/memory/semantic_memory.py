import chromadb
import uuid

from app.rag.embedding import create_embedding

client = chromadb.PersistentClient(
    path="app/chroma_db"
)

memory_collection = client.get_or_create_collection(
    name="memory"
)

def store_memory(
    session_id,
    text
):

    embedding = create_embedding(text)

    memory_collection.add(

        ids=[str(uuid.uuid4())],

        documents=[text],

        embeddings=[embedding],

        metadatas=[
            {
                "session_id": session_id
            }
        ]
    )

def retrieve_memory(
    session_id,
    query,
    top_k=3
):

    query_embedding = create_embedding(query)

    results = memory_collection.query(

        query_embeddings=[query_embedding],

        n_results=top_k,

        where={
            "session_id": session_id
        }
    )

    documents = results["documents"][0]

    return documents