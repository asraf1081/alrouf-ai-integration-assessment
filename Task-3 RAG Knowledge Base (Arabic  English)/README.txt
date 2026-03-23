# Technical Requirements Checklist

This project implements a Retrieval-Augmented Generation (RAG) system with document ingestion, vector search, and a bilingual chatbot interface.

## Checklist

| Requirement | Implementation | Filename(s) | Status |
|--------------|---------------|-------------|--------|
| **3–5 Sample Documents** | Sample documents created for testing | `data/1_warranty.txt`, `data/2_shipping.txt`, `data/3_returns.txt` | ✅ Complete |
| **Ingestion & Chunking** | Uses `DirectoryLoader` and `RecursiveCharacterTextSplitter` for document loading and splitting | `ingest.py` | ✅ Complete |
| **Embedding & Indexing** | Generates embeddings and stores them in a FAISS vector index | `ingest.py` | ✅ Complete |
| **Vector DB Storage** | Stores vector database locally | `faiss_alrouf/index.faiss`, `faiss_alrouf/index.pkl` | ✅ Complete |
| **Retrieval & Querying** | Query interface available via CLI and Web UI | `chat.py` (CLI), `app.py` (Web UI) | ✅ Complete |
| **Citations & Sources** | Displays document source metadata for transparency | `chat.py`, `app.py` | ✅ Complete |
| **Minimal Web UI** | Built using the Streamlit framework | `app.py` | ✅ Complete |
| **API Authentication** | Secure API key management using environment variables | `.env` (`GROQ_API_KEY`) | ✅ Complete |
| **Bilingual Support** | Supports English and Arabic using Llama 3.1 | `chat.py`, `app.py` | ✅ Complete |
| **Guardrails** | Strict prompt instructions to refuse out-of-scope queries | `chat.py`, `app.py` | ✅ Complete |


