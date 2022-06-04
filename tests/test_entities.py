import pytest

from src.entities import Room, Map, UndirectedGraph


@pytest.mark.parametrize("room, expected", [
    ({"id": 1, "name": "Hallway", "north": 2, "east": 7, "objects": []}, {2, 7}),
    ({"id": 7, "name": "Living room", "west": 1, "north": 4, "objects": []}, {1, 4}),
    ({"id": 5, "name": "Bedroom", "south": 2, "east": 6, "objects": [{"name": "Pillow"}]}, {2, 6})
])
def test_room_returns_linked_rooms(room, expected):
    r = Room(**room)
    assert r.get_linked_rooms() == expected


@pytest.mark.parametrize("map, id, expected", [
    (
        {
            "rooms": [
                {"id": 1, "name": "Hallway", "north": 2, "east": 7, "objects": []},
                {"id": 2, "name": "Dining Room", "north": 5, "south": 1, "west": 3, "east": 4, "objects": []},
                {"id": 3, "name": "Kitchen", "east": 2, "objects": [{"name": "Knife"}]},
                {"id": 4, "name": "Sun Room", "west": 2, "north": 6, "south": 7, "objects": []},
                {"id": 5, "name": "Bedroom", "south": 2, "east": 6, "objects": [{"name": "Pillow"}]},
                {"id": 6, "name": "Bathroom", "west": 5, "south": 4, "objects": []},
                {"id": 7, "name": "Living room", "west": 1, "north": 4, "objects": [{"name": "Potted Plant"}]}
            ]
        },
        6,
        {"id": 6, "name": "Bathroom", "west": 5, "south": 4, "objects": []}
    ),
    (
        {
            "rooms": [
                {"id": 1, "name": "Hallway", "north": 2, "east": 7, "objects": []},
                {"id": 2, "name": "Dining Room", "north": 5, "south": 1, "west": 3, "east": 4, "objects": []},
                {"id": 3, "name": "Kitchen", "east": 2, "objects": [{"name": "Knife"}]},
            ]
        },
        2,
        {"id": 2, "name": "Dining Room", "north": 5, "south": 1, "west": 3, "east": 4, "objects": []}
    ),
])
def test_map_returns_room_by_id(map, id, expected):
    m = Map(**map)
    assert m.get_room(id) == Room(**expected)


@pytest.mark.parametrize("v, neighbours", [
    (1, (2, 5, 7)),
    (0, (1,)),
])
def test_graph_set_neighbours(v, neighbours):
    graph = UndirectedGraph()
    graph.add_neighbours(v, neighbours)
    assert graph.schema_.get(v) == neighbours


@pytest.mark.parametrize("v, neighbours", [
    (1, (2, 5, 7)),
    (0, (1,)),
])
def test_graph_get_neighbours(v, neighbours):
    graph = UndirectedGraph()
    graph.schema_.update({v: neighbours})
    assert graph.get_neighbours(v) == neighbours
