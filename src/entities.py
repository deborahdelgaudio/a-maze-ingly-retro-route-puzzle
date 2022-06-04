from typing import Iterable, List, Optional

from pydantic import BaseModel


class Object_(BaseModel):
    name: str


class Room(BaseModel):
    id: int
    name: str
    north: Optional[str]
    south: Optional[str]
    west: Optional[str]
    east: Optional[str]
    objects: List[Object_] = []

    def get_linked_rooms(self):
        v_list = [self.north, self.south, self.west, self.east]
        return set([int(v) for v in v_list if v is not None])


class Map(BaseModel):
    rooms: List[Room]

    def get_room(self, id: int) -> Room:
        return [room for room in self.rooms if room.id == id][0]


class Step(BaseModel):
    id: int
    room: str
    object_collected: Optional[List[str]]


class UndirectedGraph(BaseModel):
    schema_: dict = {}

    def add_neighbours(self, v: int, neighbours: Iterable[int]):
        self.schema_.update({v: neighbours})

    def get_neighbours(self, v: int):
        return self.schema_.get(v, [])
