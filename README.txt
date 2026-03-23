# AL ROUF AI Integration Engineer Assessment

This repository contains the complete implementation of the three tasks required for the AI Integration Engineer assessment.

- **Task 1:** RFQ → CRM Automation (no‑code + optional LLM)
- **Task 2:** Quotation Microservice (Python / FastAPI / Docker)
- **Task 3:** Bilingual RAG Knowledge Base (LangChain / FAISS / Groq)

All tasks are designed with a focus on cost‑effectiveness, offline safety, and maintainability.

---

## 📁 Repository Structure
.
├── Task-1 RFQ → CRM Automation (No-Code + Optional LLM)
│ └── README.md # Automation overview (Make.com scenario)
├── Task-2 Quotation Microservice
│ ├── alrouf-quote-api-code/ # FastAPI source code
│ ├── Dockerfile
│ └── requirements.txt
├── Task-3 RAG Knowledge Base (Arabic English)
│ ├── alrouf-rag-ai-code/ # RAG source code
│ ├── .env.example.txt
│ ├── data/ # Sample bilingual documents
│ ├── faiss_alrouf/ # Pre‑built FAISS vector index
│ └── requirements.txt
└── .gitignore

text

---

## 🚀 Task 1 – RFQ → CRM Automation

**Technology:** Make.com, Google Sheets, Google Drive, Slack, Gmail

This workflow automatically processes incoming RFQ emails:

1. **Trigger:** New email in a designated inbox.
2. **Parse:** Extracts fields (customer, items, quantities) using Make.com’s native JSON parser.
3. **CRM Mock:** Logs data to a Google Sheet with Riyadh timezone.
4. **Archiving:** Saves attachments to Google Drive folders named by RFQ ID.
5. **Alerts:** Sends a Slack message to the #rfq‑alerts channel.
6. **Auto‑reply:** Drafts a bilingual (English/Arabic) acknowledgment email.

The Make.com scenario is exported as a blueprint (included in the submission ZIP). To replicate, import the blueprint and configure your own Google Workspace, Slack, and email credentials.

---

## 🐍 Task 2 – Quotation Microservice

**Technology:** Python 3.10, FastAPI, Pydantic, Docker, pytest

A lightweight REST API that calculates quotations with a fixed 20% margin and generates a bilingual email draft.

### Features
- **POST /quote** – Accepts a list of items with unit cost and quantity, returns total price and email draft.
- **Offline‑safe** – No external dependencies required for core logic.
- **Mock email draft** – Can be replaced with real LLM (OpenAI) via environment variable.
- **OpenAPI docs** – Available at `/docs` when running.

### Quick Start (with Docker)
```bash
cd Task-2\ Quotation\ Microservice
docker build -t alrouf-quote-api .
docker run -p 8000:8000 alrouf-quote-api
The API will be available at http://localhost:8000.

Local Development (without Docker)
bash
cd Task-2\ Quotation\ Microservice/alrouf-quote-api-code
pip install -r requirements.txt
uvicorn main:app --reload
Testing
bash
pytest tests/
🧠 Task 3 – Bilingual RAG Knowledge Base
Technology: LangChain, FAISS, HuggingFace embeddings (local), Groq LPU (Llama 3.1), Streamlit

A retrieval‑augmented generation system that answers questions (English or Arabic) based on a set of policy documents. It provides citations and refuses out‑of‑scope queries.

Features
Local embeddings – Uses paraphrase-multilingual-MiniLM-L12-v2 for privacy and zero cost.

Vector store – FAISS index pre‑built from sample documents (shipping & return policies).

Fast inference – Uses Groq’s Llama 3.1 API for near‑instant responses (~1.5s latency).

Bilingual – Detects query language and responds accordingly.

Citations – Returns the source document and relevant snippet.

Setup
Copy .env.example.txt to .env and add your GROQ_API_KEY.

(Optional) If you prefer OpenAI, modify chat_openai.py and set your OPENAI_API_KEY.

Run the Streamlit UI
bash
cd Task-3\ RAG\ Knowledge\ Base\ \(Arabic\ English\)/alrouf-rag-ai-code
pip install -r requirements.txt
streamlit run app.py
Ingest New Documents (if needed)
bash
python ingest.py --docs ./data
This will rebuild the FAISS index.

API Endpoint (if using FastAPI version)
The folder also includes app.py (Streamlit) and chat.py (FastAPI). To run the FastAPI version:

bash
uvicorn chat:app --reload
Then query via POST /ask.



