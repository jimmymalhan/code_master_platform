import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import date
from app.db import Base  # Ensure this imports all necessary models indirectly or directly

# Import models
from app.models.user import User
from app.models.subscription import Subscription
from app.models.order import Order
from app.models.event import Event

# Configure test database and engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_salesbrick.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Session factory, scoped to ensure uniqueness per thread
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Fixture to set up and tear down the database
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Creates all tables
    yield
    Base.metadata.drop_all(bind=engine)  # Clean up after tests

@pytest.fixture(scope="function")
def db_session():
    """Create a session for a test, rollback changes after the test."""
    session = Session()
    yield session
    session.rollback()  # Ensure each test is isolated
    session.close()

# Test functions
def test_create_order(db_session):
    """Test creating an order and ensure all properties are correct."""
    user = User(username='testbuyer', role='buyer')
    db_session.add(user)
    db_session.commit()
    subscription = Subscription(buyer_id=user.id, seller_id=user.id, state='active', monthly_revenue=200.0)
    db_session.add(subscription)
    db_session.commit()
    order = Order(subscription_id=subscription.id, start_date=date(2022, 1, 1), end_date=date(2022, 12, 31), total=1200, state='closed')
    db_session.add(order)
    db_session.commit()

def test_create_event(db_session):
    """Test creating an event linked to an order and verify its correct creation."""
    order = Order(subscription_id=1, start_date=date(2022, 1, 1), end_date=date(2022, 12, 31), total=1200, state='closed')
    db_session.add(order)
    db_session.commit()
    event = Event(order_id=order.id, type='ORDER_CLOSED_WON', timestamp=date(2022, 1, 2))
    db_session.add(event)
    db_session.commit()
