import app
import pytest

@pytest.fixture
def client():
    app.app.testing = True
    return app.app.test_client()

def test_addition(client):
    response = client.post('/add', json={"num1": 2, "num2": 3})
    assert response.status_code == 200
    assert response.json == {"result": 5}

def test_invalid_input(client):
    response = client.post('/add', json={"num1": "abc", "num2": 3})
    assert response.status_code == 400
    assert "error" in response.json

def test_missing_fields(client):
    response = client.post('/add', json={"num1": 2})
    assert response.status_code == 400
    assert "error" in response.json
