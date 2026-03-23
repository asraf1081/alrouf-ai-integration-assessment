from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

def test_generate_quote_success():
    """Test that the quote endpoint calculates math correctly."""
    payload = {
        "customer_name": "Test Client",
        "items": [
            {
                "item_name": "Test Lamp",
                "unit_cost": 100.0,
                "margin_pct": 0.20,
                "qty": 10
            }
        ]
    }
    
    response = client.post("/quote", json=payload)
    
    # 1. Check that the request was successful (200 OK)
    assert response.status_code == 200
    
    data = response.json()
    
    # 2. Check the math (100 * 1.20 * 10 = 1200)
    assert data["grand_total"] == 1200.0
    
    # 3. Check that the email draft was generated
    assert "email_draft" in data
    assert "Test Client" in data["email_draft"]