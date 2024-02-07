from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.trucks.trucks import Trucks
from models.constants.status import Status
from datetime import datetime, timedelta


class Route:
    _format = '%b %dst %H:%Mh'
    def __init__(self, route_id: int, date_time_departure: datetime, start_location: Locations, *other_locations: Locations) -> None:
        self._route_id = route_id
        self._date_time_departure = self.format_datetime(date_time_departure)
        self._start_location = start_location
        self._other_locations = other_locations
        self._status = Status.IN_PROGRESS
        self._locations: list[Locations] = []
        self._truck_list: list[Trucks] = []
        if datetime.now() < self._date_time_departure:
            self._status = Status.STANDING
        elif datetime.now() >= self._date_time_departure:
            self._status = Status.IN_PROGRESS
        elif datetime.now() >= self._other_locations[-1]:
            self._status = Status.FINISHED
        
        self._locations.append(self._start_location)
        self._locations.extend(self._other_locations) 


        

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
    
    @property
    def status(self):
        return self._status
    
    @property
    def date_time_departure(self):
        return self._date_time_departure
    
    def format_datetime(self, input_datetime: str) -> str:
        parsed_datetime = datetime.strptime(input_datetime, "%Y%m%dT%H%M")
        formatted_datetime = parsed_datetime.strftime("%b %dst %H:%Mh")

        return parsed_datetime

    
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
        
        return f'\nTotal distance: {total_distance}'
    

    def __str__(self) -> str:
        departure_str = self._date_time_departure
        route_str = f"{self._start_location} ({departure_str})"
        current_time = self._date_time_departure
        total_distance = 0

        #for location in self._other_locations:
        for i in range(len(self._locations)-1):
            current_location = self._locations[i]
            next_location = self._locations[i+1]
            distance = getattr(Locations, current_location.lower())[next_location]

            time_delta_hours = distance / 87 
            arrival_time = current_time + timedelta(hours=time_delta_hours)
            arrival_str = arrival_time
            route_str += f" → {self._locations[i+1]} ({arrival_str})"
            current_time = arrival_time
            
            total_distance += distance
            
            
        
        return f'{total_distance}\n{route_str}\n'
            #'Current locations: {}'