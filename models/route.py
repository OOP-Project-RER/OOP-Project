from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.trucks.trucks import Trucks

class Route:
    def __init__(self, route_id: int, start_location: Locations, *other_locations: Locations) -> None:
        self._route_id = route_id
        self._start_location = start_location
        self._other_locations = other_locations
        self._locations: list[Locations] = []
        self._truck_list: list[Trucks] = []
        

    @property
    def route_id(self):
        return self._route_id
    
    @property
    def start_location(self):
        return self._start_location
    
    @property
    def other_locations(self):
        return self._other_locations
    
    @property
    def locations(self):
        return self._locations
    
    def add_location(self):
        self._locations.clear() 
        self._locations.append(self._start_location)
        self._locations.extend(self._other_locations)        

    def calculate_distance_and_time(self):
        total_distance = 0
    
        for i in range(len(self._locations) - 1):
            current_location = self._locations[i]
            next_location = self._locations[i + 1]
            distance = getattr(Locations, current_location.lower())[next_location]
            total_distance += distance
        
        total_time = total_distance / 87
        total_time = "{:.2f}".format(total_time)
        
        return total_distance, total_time