# Alrouf Quotation Microservice (Task 2)

## Project Overview
This is a production-ready FastAPI microservice built for Alrouf's sales team to automate the calculation of RFQ (Request for Quote) line items and generate bilingual (English/Arabic) email drafts for customers.

## Key Features
* **Automated Logic**: Implements the required formula: `price per line = unit_cost × (1 + margin_pct) × qty`.
* **Bilingual AI Support**: Generates professional email drafts in both English and Arabic.
* **Interactive API Docs**: Auto-generated OpenAPI (Swagger) documentation for easy integration.
* **Containerized**: Fully Dockerized for "works everywhere" deployment.
* **Tested**: Includes a comprehensive test suite using `pytest`.

## Project Structure
* `app/main.py`: The FastAPI application and endpoint definitions.
* `app/models.py`: Data validation schemas using Pydantic.
* `app/services.py`: Core business logic and LLM integration.
* `tests/`: Automated unit tests for mathematical accuracy.
* `Dockerfile`: Container configuration for local and cloud deployment.

## How to Run (Local)
1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python -m uvicorn app.main:app --reload`
3. Access documentation: `http://127.0.0.1:8000/docs`

## How to Run (Docker)
1. Build image: `docker build -t quotation-service .`
2. Run container: `docker run -p 8000:8000 quotation-service`
