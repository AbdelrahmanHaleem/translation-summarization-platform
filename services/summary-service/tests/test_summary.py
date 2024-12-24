import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_summarization():
    response = client.post("/summarize", json={"text": "This is a long text that needs to be summarized. It should be concise and cover the main points."})
    assert response.status_code == 200
    assert "summary" in response.json()

