from .map_site import MapSite
from .direction import Direction


class Room(MapSite):
    def __init__(self, room_number: int) -> None:
        self._room_number = room_number
        self._sides = {}

    def get_side(self, direction: Direction) -> MapSite:
        raise NotImplementedError

    def set_side(self, direction: Direction, site: MapSite) -> None:
        raise NotImplementedError

    def enter(self) -> None:
        raise NotImplementedError
