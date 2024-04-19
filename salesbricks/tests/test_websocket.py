# test_websocket.py
from starlette.websockets import WebSocketDisconnect
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_websocket():
    """Test WebSocket endpoint for correct echo responses."""
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("hello")
        data = websocket.receive_text()
        assert data == "Echo: hello"