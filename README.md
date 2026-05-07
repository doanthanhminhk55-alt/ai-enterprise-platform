# ai-enterprise-platform

Phase 1
python -m venv venv
pip install fastapi uvicorn langchain openai qdrant-client python-dotenv pypdf tiktoken sentence-transformers
run server: uvicorn app.main:app --reload
-> http://127.0.0.1:8000 | http://127.0.0.1:8000/docs (Swagger)
pip install groq
https://console.groq.com/keys?utm_source=chatgpt.com

Phase 2
pip install groq qdrant-client sentence-transformers pypdf python-multipart numpy
pip install chromadb groq sentence-transformers pypdf python-multipart fastapi uvicorn numpy