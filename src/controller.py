from typing import List

from src.entities import Map, Step
from src.search_objects_use_case import search_objects


def find_valid_path(map: Map, start_room_id: int, objects_to_collect: List[str], logger) -> List[Step]:
    logger.info(f"Input Start Room ID={start_room_id}, Input Objects to collect={objects_to_collect}")

    steps: List[Step] = search_objects(
        root=start_room_id,
        objects_to_collect=objects_to_collect,
        map=map
    )

    steps_rows = "\n".join(["{id},{room},{object_collected}".format(**step.dict()) for step in steps])
    logger.info(f"\nID,Room,Object Collected\n{steps_rows}")

    return steps
