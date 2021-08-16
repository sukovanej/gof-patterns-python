from .room import Room

class Maze:
    def __init__(self) -> None:
        ...

    def add_room(self, room: Room) -> None:
        ...

    def get_room(self, room_number: int) -> Room:
        ...