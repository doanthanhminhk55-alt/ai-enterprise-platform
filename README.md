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

PHASE 4 Multi-Agent AI System

User Question
      ↓
Planner Agent
      ↓
Retriever Agent
      ↓
Research Agent
      ↓
Critic Agent
      ↓
Final Answer Agent

Planner Agent
Retriever Agent
Critic Agent
Summarizer Agent
Tool Router
Reflection Loop
ReAct workflow

pip install langchain-community


Phase 5 — Redis + Long-Term Memory + Session AI
“multi-agent AI” to “stateful production AI platform”
User Chat
    ↓
Session Memory
    ↓
Redis Cache
    ↓
Long-term Semantic Memory
    ↓
Relevant Memory Retrieval
    ↓
LangGraph Agents

D:\redis\Redis-x64-5.0.14.1
run redis-server.exe

run redis-cli.exe 
run ping

pip install redis


AI Enterprise Platform — Tóm Tắt Trả Lời Phỏng Vấn
1. Tổng quan project

“Em xây dựng một nền tảng AI Enterprise Platform theo kiến trúc production sử dụng FastAPI, LangGraph, ChromaDB, Redis và Groq LLM.”

Hệ thống có khả năng:

upload PDF
chat với document
semantic search
multi-agent AI workflow
memory theo session
streaming AI response
long-term semantic memory
2. Kiến trúc tổng thể
Frontend (HTML/CSS/JS)
        ↓
FastAPI Backend
        ↓
LangGraph Multi-Agent Workflow
        ↓
Memory System (Redis + Semantic Memory)
        ↓
RAG Retrieval Pipeline
        ↓
ChromaDB Vector Database
        ↓
Groq LLM
3. Flow hoạt động chính
Upload PDF
Upload PDF
    ↓
Extract text
    ↓
Chunking
    ↓
Embedding
    ↓
Store vào ChromaDB
Chat với AI
User Question
    ↓
Semantic Retrieval
    ↓
Multi-Agent Processing
    ↓
LLM Generation
    ↓
Streaming Response
4. RAG Pipeline là gì?

RAG (Retrieval-Augmented Generation) là kiến trúc:

retrieve dữ liệu liên quan trước
sau đó mới generate answer bằng LLM

Mục tiêu:

giảm hallucination
tăng độ chính xác
grounding AI bằng dữ liệu thật
5. Vì sao phải chunking?

LLM không thể xử lý document quá lớn hiệu quả.

Nên em:

chia document thành nhiều đoạn nhỏ
có overlap giữa các chunks
tăng chất lượng semantic retrieval
6. Embedding là gì?

Embedding là:

chuyển text thành vector số

Ví dụ:

"AI is powerful"

↓

[0.123, -0.555, ...]

Mục đích:

semantic similarity search
vector retrieval
7. Vì sao dùng ChromaDB?

Em dùng ChromaDB vì:

lightweight
dễ setup local
hỗ trợ persistent vector storage
phù hợp cho AI RAG systems

Dùng để:

lưu embeddings
semantic search
long-term memory retrieval
8. Multi-Agent Architecture

Em xây dựng hệ thống gồm nhiều AI agents:

Planner Agent
Retriever Agent
Research Agent
Critic Agent
Final Answer Agent
9. Chức năng từng Agent
Planner Agent

Phân tích câu hỏi và lập kế hoạch reasoning.

Retriever Agent

Tìm semantic context liên quan trong vector database.

Research Agent

Phân tích sâu nội dung đã retrieve.

Critic Agent

Review kết quả AI:

hallucination
reasoning yếu
thiếu dữ kiện
Final Agent

Tạo câu trả lời cuối cùng đã được refine.

10. Vì sao dùng Multi-Agent?

Ưu điểm:

reasoning tốt hơn
giảm hallucination
workflow rõ ràng
dễ mở rộng
dễ orchestration
11. Vai trò của LangGraph

Em dùng LangGraph để:

orchestration AI agents
quản lý workflow
quản lý state giữa agents
12. Workflow LangGraph
Memory
   ↓
Planner
   ↓
Retriever
   ↓
Researcher
   ↓
Critic
   ↓
Final
13. Memory System

Em implement:

short-term memory
long-term semantic memory
14. Short-Term Memory

Dùng:

Redis

Mục đích:

lưu chat history
session conversations
temporary memory
15. Long-Term Memory

Dùng:

ChromaDB semantic memory collection

Mục đích:

semantic recall
AI personalization
persistent memory
16. Ví dụ memory retrieval
User:
"Tên tôi là Minh"

Sau đó hỏi:
"Tôi tên gì?"

AI sẽ retrieve semantic memory để trả lời.

17. Streaming Response

Em implement:

realtime token streaming

Sử dụng:

FastAPI StreamingResponse
Groq streaming API

Ưu điểm:

UX giống ChatGPT
giảm cảm giác delay
18. Frontend

Frontend em viết bằng:

HTML
CSS
Vanilla JavaScript

Có:

upload PDF
AI chat
streaming UI
session support
19. Vì sao không dùng framework frontend?

Em muốn:

thể hiện frontend fundamentals
lightweight
dễ demo
không phụ thuộc framework
20. Session-Based AI

Mỗi session:

có memory riêng
có chat history riêng
retrieve context riêng

Ví dụ:

session_id=minh
21. API Design

Các APIs chính:

POST /upload
GET  /chat
GET  /chat-stream
22. Vì sao dùng Groq?

Em dùng Groq vì:

inference rất nhanh
latency thấp
hỗ trợ open-source LLM tốt
streaming tốt

Model sử dụng:

Llama 3
Mixtral
23. Những kỹ thuật AI đã sử dụng
Kỹ thuật	Có
RAG	✅
Embedding	✅
Semantic Search	✅
Vector DB	✅
LangGraph	✅
Multi-Agent AI	✅
Streaming AI	✅
Redis Memory	✅
ChromaDB	✅
Prompt Engineering	✅
FastAPI	✅
24. Khó khăn kỹ thuật lớn nhất
Khó khăn 1

Làm retrieval đủ chính xác.

Giải pháp:

semantic embedding
chunk overlap
top-k retrieval
Khó khăn 2

Giảm hallucination.

Giải pháp:

critic agent
grounding context
retrieval-first prompting
Khó khăn 3

Giữ conversation memory.

Giải pháp:

Redis short-term memory
semantic long-term memory
25. Nếu scale production sẽ làm gì?

Nếu scale lớn hơn em sẽ thêm:

async workers
Kafka/RabbitMQ
reranking
hybrid search
observability
Kubernetes
evaluation pipelines
26. Em học được gì từ project?

Project giúp em hiểu:

AI production architecture
agent orchestration
vector database
memory systems
streaming inference
RAG optimization
AI workflow design
27. Câu chốt mạnh khi phỏng vấn

“Em xây dựng một hệ thống multi-agent RAG AI platform sử dụng FastAPI, LangGraph, ChromaDB, Redis memory và Groq streaming inference theo kiến trúc production-style.”

28. Version senior hơn

“Em thiết kế và triển khai một nền tảng AI stateful multi-agent sử dụng LangGraph orchestration, semantic retrieval với ChromaDB, Redis conversational memory và streaming inference để phục vụ production-style RAG workflows.”