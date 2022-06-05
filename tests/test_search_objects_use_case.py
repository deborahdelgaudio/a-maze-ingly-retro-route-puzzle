import pytest

from src.entities import Map, Step
from src.search_objects_use_case import search_objects


MAP1 = {
    "rooms": [
        {"id": 1, "name": "Hallway", "north": 2, "objects": []},
        {"id": 2, "name": "Dining Room", "south": 1, "west": 3, "east": 4, "objects": []},
        {"id": 3, "name": "Kitchen", "east": 2, "objects": [{"name": "Knife"}]},
        {"id": 4, "name": "Sun Room", "west": 2, "objects": [{"name": "Potted Plant"}]}
    ]
}

MAP2 = {
    "rooms": [
        {"id": 1, "name": "Hallway", "north": 2, "east": 7, "objects": []},
        {"id": 2, "name": "Dining Room", "north": 5, "south": 1, "west": 3, "east": 4, "objects": []},
        {"id": 3, "name": "Kitchen", "east": 2, "objects": [{"name": "Knife"}]},
        {"id": 4, "name": "Sun Room", "west": 2, "north": 6, "south": 7, "objects": []},
        {"id": 5, "name": "Bedroom", "south": 2, "east": 6, "objects": [{"name": "Pillow"}]},
        {"id": 6, "name": "Bathroom", "west": 5, "south": 4, "objects": []},
        {"id": 7, "name": "Living room", "west": 1, "north": 4, "objects": [{"name": "Potted Plant"}]}
    ]
}


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
