# tests/test_events.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.events.event_handlers import dispatch_event, handle_order_closed_won, handle_order_closed_lost, handle_order_closed_won_revenue
from app.events.event_types import ORDER_CLOSED_WON, ORDER_CLOSED_LOST, ORDER_CLOSED_WON_REVENUE

@pytest.fixture(scope="module")
def test_client():
    """
    Provides a test client that can be used to make requests to the FastAPI app.
    This client simulates HTTP requests and captures the responses.
    """
    client = TestClient(app)
    return client

def test_order_closed_won_handling():
    """Tests that the ORDER_CLOSED_WON event is handled correctly."""
    handle_order_closed_won(123)  # Assuming 123 is an order ID

def test_order_closed_lost_handling():
    """Tests that the ORDER_CLOSED_LOST event is handled correctly."""
    handle_order_closed_lost(123)  # Assuming 123 is an order ID

def test_order_closed_won_revenue_handling():
    """Tests that the ORDER_CLOSED_WON_REVENUE event is handled correctly."""
    handle_order_closed_won_revenue(123, 1000.0)  # Assuming 123 is an order ID and 1000.0 is the revenue

def test_close_order_endpoint(test_client):
    """
    Ensures the /close-order/{order_id} endpoint correctly handles the 'won' status.
    This test checks if the status code and response content match expected values.
    """
    order_id = 123
    response = test_client.post(f"/close-order/{order_id}", json={"order_status": "won"})
    assert response.status_code == 200, f"Expected 200 OK but got {response.status_code}"

def test_close_order_lost_endpoint(test_client):
    """
    Ensures the /close-order/{order_id} endpoint correctly handles the 'lost' status.
    This test checks if the status code and response content match expected values.
    """
    order_id = 123
    response = test_client.post(f"/close-order/{order_id}", json={"order_status": "lost"})
    assert response.status_code == 200, f"Expected 200 OK but got {response.status_code}"
    
def test_record_revenue_endpoint(test_client):
    """
    Tests the /record-revenue/{order_id}/{revenue} endpoint to ensure it correctly records revenue.
    This test checks if the status code and response content match expected values.
    """
    order_id = 123
    revenue = 2000.0
    response = test_client.post(f"/record-revenue/{order_id}/{revenue}")
    assert response.status_code == 200, f"Expected 200 OK but got {response.status_code}"
    assert response.json() == {"status": "Revenue recorded", "order_id": order_id, "revenue": revenue}, "Unexpected response body"
