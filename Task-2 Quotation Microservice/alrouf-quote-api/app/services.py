import os
from openai import OpenAI

# Initialize OpenAI client (it will use OPENAI_API_KEY if available)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "dummy-key"))

def calculate_totals(items):
    """Calculates individual line totals and the grand total."""
    line_totals = []
    grand_total = 0.0
    
    for item in items:
        # Logic: price per line = unit_cost x (1 + margin_pct) x qty
        line_price = item.unit_cost * (1 + item.margin_pct) * item.qty
        line_price = round(line_price, 2)
        
        line_totals.append({"item_name": item.item_name, "line_total": line_price})
        grand_total += line_price
        
    return line_totals, round(grand_total, 2)

def generate_email_draft(customer_name: str, grand_total: float, use_mock: bool = True) -> str:
    """Generates a bilingual email draft using OpenAI or a Mock response."""
    
    # Run locally without API keys requirement
    if use_mock or not os.getenv("OPENAI_API_KEY"):
        return f"""
Dear {customer_name},
Thank you for your request. The total price for your quotation is ${grand_total}. Delivery will be within 4 weeks.

عزيزي {customer_name}،
شكراً لطلبك. إجمالي السعر لعرض السعر الخاص بك هو ${grand_total}. سيكون التسليم خلال 4 أسابيع.
"""
        
    # Real OpenAI Call (Requires OPENAI_API_KEY in .env)
    prompt = f"Write a short, professional bilingual (English/Arabic) email to {customer_name} confirming a quote total of ${grand_total}. Mention delivery is 4 weeks."
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating email: {str(e)}"