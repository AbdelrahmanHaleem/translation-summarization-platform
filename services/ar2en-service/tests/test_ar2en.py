import pytest
from app import app
from flask.testing import FlaskClient

@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client

def test_translation(client):
    response = client.post("/translate/ar2en", json={"text": "مرحباً، كيف حالك؟"})
    assert response.status_code == 200
    assert "translated_text" in response.json

