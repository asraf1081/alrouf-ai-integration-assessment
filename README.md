# Project Title: Alrouf AI Integration Engineer Assessment

## 📋 Overview
This repository contains the complete implementation of the three tasks required for the AI Integration Engineer assessment, designed with a focus on cost‑effectiveness, offline safety, and maintainability.

---

## 🚀 Task Details

### 🔹 Task 1: RFQ Automation System
* [cite_start]**Objective:** Automate incoming RFQ emails the second they are received without manual intervention[cite: 5].
* **Requirements:**
    * [cite_start]Make.com webhook (Custom Mailhook)[cite: 1, 2].
    * [cite_start]Google Sheets for database logging[cite: 13, 14].
    * [cite_start]Google Drive for attachment archiving[cite: 31].
    * [cite_start]Slack for internal notifications[cite: 34].
    * [cite_start]Gmail for auto-replies[cite: 23].
* **Key Deliverables:**
    * [cite_start]Extracts fields like item, quantity, contact_name, and location via built-in JSON parsing to ensure 100% precision[cite: 8, 11].
    * [cite_start]Logs data to the "RFQ Logs" Google Sheet, localized to Riyadh time[cite: 15, 16].
    * [cite_start]Sends a mock CRM payload using an HTTP POST request containing the Opportunity Name, Product, and Quantity[cite: 20, 21].
    * [cite_start]Sends a professionally drafted bilingual auto-reply in Arabic and English using raw HTML formatting[cite: 24, 26].
    * [cite_start]Iterates and uploads separate email files to an "RFQ Attachments" Google Drive folder[cite: 30, 31].
    * [cite_start]Triggers a final alert to the #rfq-alerts Slack channel featuring the client name and requested item[cite: 35, 36].

### 🔹 Task 2: Quotation Microservice
* [cite_start]**Objective:** Provide a RESTful API built with FastAPI to handle lighting product quotations, automated margin calculations, and an AI-powered email drafting feature[cite: 61, 62].
* **Requirements:**
    * [cite_start]FastAPI and Uvicorn for endpoints and high-speed serving[cite: 64].
    * [cite_start]Pydantic for strict data type validation[cite: 51, 64].
    * [cite_start]OpenAI and python-dotenv for AI integration and security[cite: 65, 66].
    * [cite_start]Docker to ensure parity between development and production environments[cite: 52].
* **Key Deliverables:**
    * [cite_start]Isolates core calculation logic within app/services.py for maintainability[cite: 54].
    * [cite_start]Calculates line items using the formula unit_cost * (1 + margin_pct) * qty, rounding the grand total to two decimal places[cite: 55].
    * [cite_start]Contains a Mock LLM Switch that utilizes a local template for offline testing, while remaining prepared to connect to OpenAI via a .env file[cite: 57, 58].
    * [cite_start]Verifies a 20% margin calculation on a 100 unit cost for 120 items (totaling 14,400) using pytest[cite: 60].
    * [cite_start]Exposes an interactive Swagger UI for testing at http://120.0.0.1:8000/docs[cite: 68].

### 🔹 Task 3: AI Knowledge Base (RAG System)
* [cite_start]**Objective:** Provide a production-ready, bilingual (English and Arabic) Retrieval-Augmented Generation system allowing users to query company policies with cited responses[cite: 70, 71].
* **Requirements:**
    * [cite_start]Langchain ecosystem (langchain, langchain-community, langchain-core)[cite: 92].
    * [cite_start]FAISS (faiss-cpu) to store text chunks as math vectors[cite: 93].
    * [cite_start]HuggingFace sentence-transformers for local, zero-cost processing[cite: 94].
    * [cite_start]Groq (langchain-groq) to connect to the Llama 3.1 model[cite: 95].
    * [cite_start]Streamlit for the web user interface[cite: 96].
* **Key Deliverables:**
    * [cite_start]Loads and splits documents into 500-character chunks with a 50-character overlap[cite: 73].
    * [cite_start]Generates local vector embeddings for $0.00 cost using the HuggingFace paraphrase-multilingual-MiniLM-L12-v2 model[cite: 74, 75].
    * [cite_start]Leverages the Llama 3.1-8b-instant model via Groq for high-speed cloud generation[cite: 76, 85].
    * [cite_start]Maintains a total user latency of < 1.5 seconds per query[cite: 86].
    * [cite_start]Runs utilizing an ingest.py script to build the FAISS index and an app.py script to launch the bilingual assistant[cite: 89, 90].
