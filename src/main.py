import logging
from typing import List

from pydantic import BaseModel, root_validator
from fastapi import FastAPI

from src import controller
from src.entities import Map, Step


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
def healthcheck():
    return {"Healthcheck": True}


class FindPathRequestBody(BaseModel):
    map: Map
    start_room_id: int
    objects_to_collect: List[str]

    @root_validator
    def validate_start_room_id(cls, values):
        rooms = values.get("map").rooms
        valid_ids = [int(room.id) for room in rooms]
        if values.get("start_room_id") not in valid_ids:
            raise ValueError(f"{values.get('start_room_id')} is not in the map!")
        return values

    @root_validator
    def validate_objects_to_collect(cls, values):
        rooms = values.get("map").rooms
        objects_in_map = set([o.name for room in rooms for o in room.objects])
        if not set(values.get("objects_to_collect")).issubset(objects_in_map):
            raise ValueError(f"Objects requested are not in the map!")
        return values

    class Config:
        schema_extra = {
            "example": {
                "map": {
                    "rooms": [
                        {"id": 1, "name": "Hallway", "north": 2, "objects": []},
                        {"id": 2, "name": "Dining Room", "south": 1, "west": 3, "east": 4, "objects": []},
                        {"id": 3, "name": "Kitchen", "east": 2, "objects": [{"name": "Knife"}]},
                        {"id": 4, "name": "Sun Room", "west": 2, "objects": [{"name": "Potted Plant"}]}
                    ]
                },
                "start_room_id": 2,
                "objects_to_collect": ["Knife", "Potted Plant"]
            }
        }


@app.post("/puzzle/find/path", response_model=List[Step])
def find_valid_path(body: FindPathRequestBody):
    result = controller.find_valid_path(
        map=body.map,
        start_room_id=body.start_room_id,
        objects_to_collect=body.objects_to_collect,
        logger=logger
    )
    return result
