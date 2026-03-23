from pydantic import BaseModel
from typing import List

# --- Requests ---
class LineItem(BaseModel):
    item_name: str
    unit_cost: float
    margin_pct: float  # e.g., 0.20 for 20%
    qty: int

class QuoteRequest(BaseModel):
    customer_name: str
    items: List[LineItem]

# --- Responses ---
class LineItemTotal(BaseModel):
    item_name: str
    line_total: float

class QuoteResponse(BaseModel):
    line_totals: List[LineItemTotal]
    grand_total: float
    email_draft: str