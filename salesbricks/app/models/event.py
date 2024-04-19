# event.py
# Purpose: This file contains the Event model, which represents an event that occurred in the system.

from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base  # Import Base from the centralized location

class Event(Base):
    """ Model representing an event that occurred in the system."""
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    type = Column(String, nullable=False)  # Type of event (e.g., ORDER_CLOSED_WON)
    timestamp = Column(DateTime, nullable=False)  # Time of the event

    def __repr__(self):
        return f"<Event(order_id={self.order_id}, type={self.type})>"
