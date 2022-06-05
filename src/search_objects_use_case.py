from typing import List, Tuple

from src.entities import UndirectedGraph, Map, Step


def _dfs(graph: UndirectedGraph, objects_to_collect: List[str], map: Map):
    visited = []

    def run(room_id: int, path: List[Tuple[int, int]], pocket: List[Tuple[int, str]]):
        if not objects_to_collect:
            return

        visited.append(room_id)

        # Collect objects in room
        room = map.get_room(room_id)
        for object in room.objects:
            if object.name in objects_to_collect:
                objects_to_collect.remove(object.name)
                pocket.append((room_id, object.name))

        # Recursively visit neighbours and save path
        for neighbour in graph.get_neighbours(room_id):
            if objects_to_collect and neighbour not in visited:
                path.append((room_id, neighbour))
                run(neighbour, path, pocket)
                if objects_to_collect:
                    path.append((neighbour, room_id))

    return run


def search_objects(root: int, objects_to_collect: List[str], map: Map) -> List[Step]:
    graph = UndirectedGraph()
    for room in map.rooms:
        graph.add_neighbours(room.id, room.get_linked_rooms())

    path = []
    pocket = []
    execute_search = _dfs(graph, objects_to_collect, map)
    execute_search(root, path, pocket)

    steps = [root]
    for step in path:
        steps.append(step[1])
    output = [
        Step(
            id=step,
            room=map.get_room(step).name,
            object_collected=[item[1] for item in pocket if item[0] == step]
        )
        for step in steps
    ]

    return output
