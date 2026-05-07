from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def create_embedding(text: str):

    embeeding = model.encode(text)

    return embeeding.tolist()