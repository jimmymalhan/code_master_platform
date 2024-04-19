# app/api/router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/subscriptions", tags=["Subscriptions"])
async def read_subscriptions():
    """Retrieve all subscriptions."""
    return {"message": "Listing all subscriptions"}
