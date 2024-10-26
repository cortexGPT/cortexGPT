import pytest
from src.app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Cortex!" in response.data

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "running"}

def test_health_check_invalid_method(client):
    response = client.post('/health')
    assert response.status_code == 405
