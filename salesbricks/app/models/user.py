# user.py
# Purpose: Define the User model

from sqlalchemy import Column, Integer, String
from app.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    role = Column(String)

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role})>"
