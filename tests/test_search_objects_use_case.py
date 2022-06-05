import pytest

from src.entities import Map, Step
from src.search_objects_use_case import search_objects

from tests.conftest import MAP1, MAP2


@pytest.mark.parametrize("root, map, objects, expected_path", [
    (
        2,
        MAP1,
        ["Knife", "Potted Plant"],
        [
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=1, room="Hallway", object_collected=[]),
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=3, room="Kitchen", object_collected=["Knife"]),
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=4, room="Sun Room", object_collected=["Potted Plant"])
        ]
    ),
    (
        2,
        MAP1,
        ["Knife"],
        [
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=1, room="Hallway", object_collected=[]),
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=3, room="Kitchen", object_collected=["Knife"]),
        ]
    ),
    (
        4,
        MAP2,
        ["Knife", "Potted Plant", "Pillow"],
        [
            Step(id=4, room="Sun Room", object_collected=[]),
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=1, room="Hallway", object_collected=[]),
            Step(id=7, room="Living room", object_collected=["Potted Plant"]),
            Step(id=1, room="Hallway", object_collected=[]),
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=3, room="Kitchen", object_collected=["Knife"]),
            Step(id=2, room="Dining Room", object_collected=[]),
            Step(id=5, room="Bedroom", object_collected=["Pillow"]),
        ]
    ),
])
def test_search_objects_returns_correct_path(root, map, objects, expected_path):
    m = Map(**map)
    path = search_objects(root, objects, m)
    assert path == expected_path
