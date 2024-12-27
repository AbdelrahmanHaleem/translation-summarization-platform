import pytest
from app import app
from flask.testing import FlaskClient

@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client

def test_summarization(client):
    response = client.post("/summarize", json={"text": "This is a long text that needs to be summarized. It should be concise and cover the main points."})
    assert response.status_code == 200
    assert "summary" in response.json()