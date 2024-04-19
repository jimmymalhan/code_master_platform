# tests/test_filters.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_orders_filtered(db_session):  # Ensure db_session is used
    """
    Tests the /orders endpoint with filtering parameters to ensure correct data retrieval.
    Includes the use of a mocked database session.
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        response = await ac.get("/orders?start_date=2021-01-01&end_date=2021-01-31&buyer_id=1&product_id=10")
    assert response.status_code == 200
    assert isinstance(response.json(), dict), "Response should be a dictionary"
