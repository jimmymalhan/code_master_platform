# subscription.py
# Purpose: Define the Subscription model

from sqlalchemy import Column, Integer, String, Float
from app.db import Base  # Import Base from db module

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, nullable=False)
    seller_id = Column(Integer, nullable=False)
    state = Column(String, default='active')  # Subscription status
    monthly_revenue = Column(Float, default=0.0)  # MRR

    def __repr__(self):
        return f"<Subscription id={self.id}, state={self.state}>"
