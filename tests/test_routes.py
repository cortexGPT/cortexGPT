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
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Cortex!" in response.data

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

def test_html_template_rendering(client):  # pylint: disable=W0621
    """
    Test the home route ('/') to verify that the HTML content
    is rendered correctly with the expected '<h1>Hello, Cortex!</h1>' header.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Hello, Cortex!</h1>" in response.data
