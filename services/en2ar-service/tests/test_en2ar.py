import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_translation():
    response = client.post("/translate/en2ar", json={"text": "Hello, how are you?"})
    assert response.status_code == 200
    assert "translated_text" in response.json()

