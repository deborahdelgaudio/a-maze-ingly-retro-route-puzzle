from fastapi.testclient import TestClient
import pytest

from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_hello_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
