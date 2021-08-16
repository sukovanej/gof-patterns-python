from .direction import Direction
from .maze import Maze
from .maze_factory import MazeFactory
from .wall import Wall


class MazeGame:
    def create_maze(self, maze_factory: MazeFactory) -> Maze:
        maze = maze_factory.make_maze()
        room_1 = maze_factory.make_room(1)
        room_2 = maze_factory.make_room(2)
        door = maze_factory.make_door(room_1, room_2)

        maze.add_room(room_1)
        maze.add_room(room_2)

        room_1.set_size(Direction.north, maze_factory.make_wall())
        room_1.set_size(Direction.east, door)
        room_1.set_size(Direction.south, maze_factory.make_wall())
        room_1.set_size(Direction.west, maze_factory.make_wall())

        room_2.set_size(Direction.north, maze_factory.make_wall())
        room_2.set_size(Direction.east, maze_factory.make_wall())
        room_2.set_size(Direction.south, maze_factory.make_wall())
        room_2.set_size(Direction.west, door)

        return maze