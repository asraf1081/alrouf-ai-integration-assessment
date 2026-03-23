# Project Title: Alrouf AI Integration Engineer Assessment

## 📋 Overview
This repository contains the complete implementation of the three tasks required for the AI Integration Engineer assessment, designed with a focus on cost‑effectiveness, offline safety, and maintainability.

---

## 🚀 Task Details

### 🔹 Task 1: RFQ Automation System
* **Objective:** Automate incoming RFQ emails the second they are received without manual intervention[cite: 5].
* **Requirements:**
    * Make.com webhook (Custom Mailhook)
    * Google Sheets for database logging.
    * Google Drive for attachment archiving.
    * Slack for internal notifications.
    * Gmail for auto-replies.
* **Key Deliverables:**
    * Extracts fields like item, quantity, contact_name, and location via built-in JSON parsing to ensure 100% precision.
    * Logs data to the "RFQ Logs" Google Sheet, localized to Riyadh time.
    * Sends a mock CRM payload using an HTTP POST request containing the Opportunity Name, Product, and Quantity.
    * Sends a professionally drafted bilingual auto-reply in Arabic and English using raw HTML formatting.
    * Iterates and uploads separate email files to an "RFQ Attachments" Google Drive folder.
    * Triggers a final alert to the #rfq-alerts Slack channel featuring the client name and requested item.

### 🔹 Task 2: Quotation Microservice
* **Objective:** Provide a RESTful API built with FastAPI to handle lighting product quotations, automated margin calculations, and an AI-powered email drafting feature.
* **Requirements:**
    * FastAPI and Uvicorn for endpoints and high-speed serving.
    * Pydantic for strict data type validation.
    * OpenAI and python-dotenv for AI integration and security.
    * Docker to ensure parity between development and production environments.
* **Key Deliverables:**
    * Isolates core calculation logic within app/services.py for maintainability.
    * Calculates line items using the formula unit_cost * (1 + margin_pct) * qty, rounding the grand total to two decimal places.
    * Contains a Mock LLM Switch that utilizes a local template for offline testing, while remaining prepared to connect to OpenAI via a .env file.
    * Verifies a 20% margin calculation on a 100 unit cost for 120 items (totaling 14,400) using pytest.
    * Exposes an interactive Swagger UI for testing at http://120.0.0.1:8000/docs.

### 🔹 Task 3: AI Knowledge Base (RAG System)
* **Objective:** Provide a production-ready, bilingual (English and Arabic) Retrieval-Augmented Generation system allowing users to query company policies with cited responses.
* **Requirements:**
    * Langchain ecosystem (langchain, langchain-community, langchain-core).
    * FAISS (faiss-cpu) to store text chunks as math vectors.
    * HuggingFace sentence-transformers for local, zero-cost processing.
    * Groq (langchain-groq) to connect to the Llama 3.1 model.
    * Streamlit for the web user interface.
* **Key Deliverables:**
    * Loads and splits documents into 500-character chunks with a 50-character overlap.
    * Generates local vector embeddings for $0.00 cost using the HuggingFace paraphrase-multilingual-MiniLM-L12-v2 model.
    * Leverages the Llama 3.1-8b-instant model via Groq for high-speed cloud generation.
    * Maintains a total user latency of < 1.5 seconds per query.
    * Runs utilizing an ingest.py script to build the FAISS index and an app.py script to launch the bilingual assistant.
