from abc import ABC

from .maze import Maze
from .room import Room
from .wall import Wall
from .door import Door


class MazeFactory(ABC):
    def __init__(self) -> None:
        ...

    def make_maze(self) -> Maze:
        return Maze()

    def make_wall(self) -> Wall:
        return Wall()
    
    def make_room(self, room_number: int) -> Room:
        return Room(room_number)

    def make_door(self, room_1: Room, room_2: Room) -> Room:
        return Door(room_1, room_2)