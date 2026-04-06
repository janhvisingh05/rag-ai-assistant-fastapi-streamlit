# 🤖 RAG AI Assistant (LangChain + FastAPI + Streamlit)

An end-to-end **Retrieval-Augmented Generation (RAG)** based AI assistant that answers user queries from documents (PDFs) using semantic search and Large Language Models.

This project demonstrates how to build a **production-ready AI system** with a modular backend, interactive frontend, and intelligent document understanding.

---

## 🚀 Overview

This AI assistant allows users to:

- Upload and process PDF documents
- Ask questions based strictly on document content
- Retrieve context using vector similarity search
- Generate accurate responses using an LLM
- Maintain chat history with memory
- Enforce safety using guardrails

Unlike generic chatbots, this system **does not hallucinate** — it answers only from the provided documents.

---

## ✨ Key Features

### 📄 Document Understanding
- Extracts text from PDFs
- Splits into semantic chunks
- Stores embeddings in vector database

### 🔍 Semantic Search (RAG Core)
- Uses **LangChain + ChromaDB**
- Retrieves most relevant chunks
- Context-aware answering

### 🤖 LLM Integration
- Uses **Google Gemini (via LangChain)**
- Generates grounded responses
- Controlled via prompt engineering

### 🧠 Memory System
- Stores chat history using **SQLite**
- Enables conversational continuity

### 🛡️ Guardrails (Safety Layer)
- Input validation
- Context relevance checking
- Output filtering

### ⚡ FastAPI Backend
- Clean REST API
- Scalable architecture
- Swagger docs included

### 🎨 Streamlit Frontend
- Interactive UI
- Real-time responses
- Chat-like interface

---

## 🏗️ System Architecture

```
         ┌────────────────────┐
         │   Streamlit UI     │
         └─────────┬──────────┘
                   │
                   ▼
         ┌────────────────────┐
         │   FastAPI Backend  │
         └─────────┬──────────┘
                   │
                   ▼
         ┌────────────────────┐
         │    RAG Pipeline    │
         ├────────────────────┤
         │ Retriever (Chroma) │
         │ LLM (Gemini)       │
         │ Guardrails         │
         │ Memory (SQLite)    │
         └────────────────────┘
```

---

## 📁 Project Structure

```
ai_assistant_project/
│
├── api/                    # FastAPI backend
│   └── main.py
│
├── rag/                    # Retrieval + ingestion logic
│   ├── ingest.py
│   ├── retriever.py
│   └── pipeline.py
│
├── llm/                    # LLM integration
│   └── llm.py
│
├── database/               # Chat memory (SQLite)
│   ├── db.py
│   └── schema.sql
│
├── guardrails/             # Safety checks
│   ├── input_guard.py
│   ├── context_guard.py
│   └── output_guard.py
│
├── data/                   # Vector database (Chroma)
│
├── app.py                  # Streamlit frontend
├── config.py               # Configuration
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/rag-ai-assistant-fastapi-streamlit.git
cd rag-ai-assistant-fastapi-streamlit
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## 📄 Step 1: Ingest PDF

Convert your document into embeddings:

```bash
python -m rag.ingest
```

### 🔍 What happens internally:

- PDF is loaded  
- Text is extracted  
- Split into chunks  
- Embeddings are created  
- Stored in ChromaDB  

---

## ▶️ Step 2: Run Backend (FastAPI)

```bash
uvicorn api.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## 🎨 Step 3: Run Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 🔄 How It Works (Pipeline)

### 1. User Input  
User enters a question in Streamlit UI  

### 2. Input Guard  
- Validates input  
- Filters unsafe queries  

### 3. Retriever  
- Converts query to embedding  
- Finds top relevant chunks from ChromaDB  

### 4. Context Guard  
- Ensures retrieved content is relevant  
- Avoids noise  

### 5. LLM Generation  
- Sends context + query to Gemini  
- Generates grounded response  

### 6. Output Guard  
- Filters hallucinations  
- Ensures safe output  

### 7. Memory Storage  
- Saves conversation in SQLite  

---

## 🧪 Example Queries

### ✅ Works Well
- What is Android?  
- What is battery saver mode?  
- How to send a message?  
- How to organize home screen?  

### ❌ Will Not Work
- What is Google?  
- What is Android Studio?  
- General knowledge outside document  

---

## ⚠️ Limitations

- Answers only from ingested documents  
- No internet knowledge  
- Quality depends on document clarity  
- Single-document system (currently)  

---

## 🔮 Future Improvements

- Multi-document support  
- Hybrid search (BM25 + embeddings)  
- Streaming responses  
- Voice-based input  
- Authentication system  
- Cloud deployment (AWS / Render)  
- UI enhancements  

---

## 🛠️ Tech Stack

| Component        | Technology Used        |
|-----------------|----------------------|
| Backend         | FastAPI              |
| Frontend        | Streamlit            |
| LLM             | Google Gemini        |
| Framework       | LangChain            |
| Vector DB       | ChromaDB             |
| Embeddings      | Sentence Transformers|
| Database        | SQLite               |

---

## 📌 Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)  
- Semantic Search  
- Vector Databases  
- LLM Prompt Engineering  
- API Design  
- Full-stack AI system design  

---

## 👩‍💻 Author

**Janhvi Singh**

---

## ⭐ Support

If you found this project useful:

- ⭐ Star this repository  
- 🍴 Fork it  
- 🚀 Build on top of it  
