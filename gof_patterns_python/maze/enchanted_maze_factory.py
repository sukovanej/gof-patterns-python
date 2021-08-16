from .maze_factory import MazeFactory
from .room import Room

class EnchantedMazeFactory(MazeFactory):
    def make_room(self, room_number: int) -> Room:
        return EnchantedRoom(room_number)