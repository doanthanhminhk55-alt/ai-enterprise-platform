# ai-enterprise-platform

Phase 1
python -m venv venv
pip install fastapi uvicorn langchain openai qdrant-client python-dotenv pypdf tiktoken sentence-transformers
run server: uvicorn app.main:app --reload
-> http://127.0.0.1:8000 | http://127.0.0.1:8000/docs (Swagger)
pip install groq
https://console.groq.com/keys?utm_source=chatgpt.com

Phase 2
PDF Upload
Extract Text
Chunking
Embedding
ChromaDB
Semantic Search
Groq Answer

pip install groq qdrant-client sentence-transformers pypdf python-multipart numpy
pip install chromadb groq sentence-transformers pypdf python-multipart fastapi uvicorn numpy

Phase 3 Production AI Features
Conversation Memory
Redis Cache
LangGraph Agents
Streaming Responses
Hybrid Search
Metadata Filtering
Async Processing
AI Evaluation
Prompt Templates
Function Calling

User Question
    ↓
Conversation Memory
    ↓
Semantic Retrieval
    ↓
LangGraph Agent
    ↓
Tool Calling
    ↓
Groq Streaming Response

pip install langgraph langchain langchain-core
pip freeze > requirements.txt
