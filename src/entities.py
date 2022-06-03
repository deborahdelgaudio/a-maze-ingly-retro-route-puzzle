from typing import List

from pydantic import BaseModel


class Object(BaseModel):
    name: str


class Room(BaseModel):
    id: int
    name: str
    north: str
    south: str
    west: str
    east: str
    objects: List[Object]


class Map(BaseModel):
    rooms: List[Room]


class Step(BaseModel):
    id: int
    room: str
    object_collected: str
