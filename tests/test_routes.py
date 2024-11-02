import pytest
from src.app.app import app

@pytest.fixture
def client():
    """
    Pytest fixture to configure the test client for the Flask app.
    Sets the app to testing mode and yields the client instance.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """
    Test the home route ('/') to verify it returns a 200 status
    and contains the 'Hello, Cortex!' message in its HTML content.
    """
    response = client.get('/')
    assert response.status_code == 200

def test_submit_route(client):
    response = client.post('/submit', data={'user_input': 'test'})
    assert response.status_code == 200
    assert b'Received: test' in response.data
    
    # Edge case - Empty input
    response_empty = client.post('/submit', data={'user_input': ''})
    assert response_empty.status_code == 400
    assert b'Input is required' in response_empty.data

def test_health_check(client):
    """
    Test the health check route ('/health') to verify it returns
    a 200 status and the expected JSON response indicating server status.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "running"}

def test_health_check_invalid_method(client):  # pylint: disable=W0621
    """
    Test the health check route ('/health') to verify it returns a 405
    status code when accessed with an unsupported HTTP method (POST).
    """
    response = client.post("/health")
    assert response.status_code == 405