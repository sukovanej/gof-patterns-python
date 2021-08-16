from .maze_factory import MazeFactory
from .room import Room
from .enchanted_room import EnchantedRoom

class EnchantedMazeFactory(MazeFactory):
    def make_room(self, room_number: int) -> Room:
        return EnchantedRoom(room_number)