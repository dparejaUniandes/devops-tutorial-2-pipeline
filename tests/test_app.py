# Import sys module for modifying Python's runtime environment
# Import os module for interacting with the operating system
import os
import sys

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import pytest for writing and running tests
import pytest

# Import the Flask app instance from the main app file
from application import application


@pytest.fixture
def client():
    """A test client for the app."""
    with application.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    #assert response.json == {"message": "Hello, Flask!"}

def test_get_one_heroe(client):
    """Test the home route."""
    response = client.get('/1')
    assert response.status_code == 200
    assert response.json["name"] == "Abe Sapien"