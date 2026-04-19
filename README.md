# 🏠 Local RAG Backend

A fully **local** and **private** Retrieval-Augmented Generation (RAG) system for querying PDF documents.

## ✨ Features

- 📄 **PDF Processing**: Upload and index multiple PDFs
- 🔪 **Smart Chunking**: RecursiveCharacterTextSplitter for optimal context windows
- 🧠 **Semantic Search**: sentence-transformers for meaning-based retrieval
- 💬 **Natural Answers**: Powered by Llama 3.2 via Ollama
- 🔒 **100% Local**: No API keys, no cloud services, complete privacy
- ⚡ **Fast API**: RESTful backend with FastAPI

## 🏗️ Tech Stack

- **Backend**: FastAPI
- **Vector DB**: ChromaDB
- **LLM**: Ollama (Llama 3.2)
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **PDF Parser**: pypdf

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama**
   
   Download from [ollama.com](https://ollama.com/download)
   
`ash
   ollama pull llama3.2
`

2. **Install Python Dependencies**
   
`ash
   pip install -r requirements.txt
`

### Run the Server

`ash
python main.py
`

Server runs at http://localhost:8000

## 📖 Usage

### Upload PDFs

Place your PDF files in the ISAD/ folder, then restart the server to index them.

### Query via API

`ash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is Daily Scrum?"}'
`

### Example Response

`json
{
  "query": "What is Daily Scrum?",
  "answer": "The purpose of a Daily Scrum is to keep the team focused on the Sprint Goal, reduce unnecessary meetings, and facilitate quick problem-solving among team members.",
  "sources": [
    {
      "chunk_id": 1,
      "text": "Daily Scrum\n■ It's a time-boxed, 15-minute meeting...",
      "relevance_score": 0.855
    },
    {
      "chunk_id": 2,
      "text": "Daily Scrum\n■ The Daily Scrum is run by the developers...",
      "relevance_score": 0.666
    },
    {
      "chunk_id": 3,
      "text": "Scrum Process...",
      "relevance_score": 0.718
    }
  ],
  "metadata": {
    "model": "llama3.2",
    "chunks_retrieved": 3,
    "chunks_used": 3
  }
}
`

## 🔒 Privacy & Security

- ✅ All processing happens locally on your machine
- ✅ Documents never leave your device
- ✅ No API keys required
- ✅ No usage tracking or telemetry
- ✅ Works completely offline

## 📊 Performance

- **Response Time**: 2-5 seconds (CPU-only)
- **Capacity**: Tested with 15+ PDFs simultaneously
- **GPU**: Supported but not required (speeds up inference)

## 🛠️ Development

Built as part of my AI engineering learning journey.

Currently features:
- ✅ Local PDF ingestion
- ✅ Semantic chunking
- ✅ Vector similarity search
- ✅ Local LLM generation
- 🚧 Web UI (coming next)
- 🚧 Multi-document conversations

## 📝 License

MIT

---

**Building in public** | Follow my journey on [X/Twitter](https://twitter.com/itszeang)
