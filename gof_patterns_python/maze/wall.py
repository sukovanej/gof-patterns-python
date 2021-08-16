from .map_site import MapSite


class Wall(MapSite):
    def __init__(self) -> None:
        ...

    def enter(self) -> None:
        raise NotImplementedError