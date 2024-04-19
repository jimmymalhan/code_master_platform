# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.main import app
from app.db import Base, get_db, init_db  # Ensure all these are defined in db.py

DATABASE_URL = "sqlite:///./test_salesbricks.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Creates a session for testing, ensuring isolation and clean-up."""
    init_db()  # Ensure tables are created
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def test_client():
    """Provides a test client for the FastAPI application."""
    app.dependency_overrides[get_db] = lambda: next(get_db())
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

@pytest.fixture
def mock_dispatch_event(mocker):
    """Mocks the dispatch_event function for testing."""
    return mocker.patch('app.events.event_handlers.dispatch_event')
