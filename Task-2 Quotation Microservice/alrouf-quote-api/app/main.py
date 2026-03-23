from fastapi import FastAPI
from app.models import QuoteRequest, QuoteResponse, LineItemTotal
from app.services import calculate_totals, generate_email_draft
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = FastAPI(
    title="Alrouf Quotation Microservice",
    description="API for calculating RFQ quotes and generating bilingual email drafts.",
    version="1.0.0"
)

@app.post("/quote", response_model=QuoteResponse, summary="Generate Quotation and Email Draft")
async def generate_quote(request: QuoteRequest):
    """
    Accepts RFQ line items, calculates totals, and returns a generated email draft.
    """
    # 1. Calculate the math
    line_totals, grand_total = calculate_totals(request.items)
    
    # 2. Format the response objects
    formatted_line_totals = [LineItemTotal(**item) for item in line_totals]
    
    # 3. Generate Email (Mocked by default to run locally without keys)
    use_mock = os.getenv("USE_MOCK_LLM", "true").lower() == "true"
    email_draft = generate_email_draft(request.customer_name, grand_total, use_mock=use_mock)
    
    # 4. Return the required output
    return QuoteResponse(
        line_totals=formatted_line_totals,
        grand_total=grand_total,
        email_draft=email_draft
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)