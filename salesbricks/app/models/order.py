# order.py
from sqlalchemy import Column, Integer, Date, Float, String
from app.db import Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    buyer_id = Column(Integer)
    product_id = Column(Integer)
    
    subscription_id = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total = Column(Float, nullable=False)
    state = Column(String, default='closed')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "buyer_id": self.buyer_id,
            "product_id": self.product_id
        }