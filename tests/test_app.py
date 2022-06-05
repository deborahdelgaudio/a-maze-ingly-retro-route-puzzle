from fastapi.testclient import TestClient
import pytest

from src.main import app
from tests.conftest import MAP1


@pytest.fixture
def client():
    return TestClient(app)


def test_healthcheck_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Healthcheck": True}


class TestFindValidPathRoute:
    route = "/puzzle/find/path"
    valid_body = {"map": {**MAP1}, "start_room_id": 2, "objects_to_collect": ["Knife", "Potted Plant"]}
    valid_response = [
        {"id": 2, "room": "Dining Room", "object_collected": []},
        {"id": 1, "room": "Hallway", "object_collected": []},
        {"id": 2, "room": "Dining Room", "object_collected": []},
        {"id": 3, "room": "Kitchen", "object_collected": ["Knife"]},
        {"id": 2, "room": "Dining Room", "object_collected": []},
        {"id": 4, "room": "Sun Room", "object_collected": ["Potted Plant"]}
    ]

    def test_route_responds_successfully(self, client):
        response = client.post(self.route, json=self.valid_body)
        assert response.status_code == 200
        assert response.json() == self.valid_response

    def test_route_responds_422_for_invalid_objects(self, client):
        invalid_body = {**self.valid_body, "objects_to_collect": ["Gun"]}

        response = client.post(self.route, json=invalid_body)
        assert response.status_code == 422

    def test_route_responds_422_for_invalid_start(self, client):
        invalid_body = {**self.valid_body, "start_room_id": len(MAP1["rooms"]) + 10}

        response = client.post(self.route, json=invalid_body)
        assert response.status_code == 422
