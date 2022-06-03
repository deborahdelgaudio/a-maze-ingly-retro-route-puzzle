from typing import List

from pydantic import BaseModel
from fastapi import FastAPI

from src.entities import Map, Object, Step

app = FastAPI()


@app.get("/")
def healthcheck():
    return {"Healthcheck": True}


class FindRouteRequestBody(BaseModel):
    map: Map
    start_room_id: int
    objects_to_collect: List[Object]

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
def find_valid_path(body: FindRouteRequestBody):
    pass
