from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.trucks.trucks import Trucks

class Route:
    def __init__(self, route_id: int) -> None:
        self._route_id = route_id
        self._locations: list[Locations] = []
        self._truck_list: list[Trucks] = []

    @property
    def route_id(self):
        return self._route_id
    
    @property
    def locations(self):
        return self._locations