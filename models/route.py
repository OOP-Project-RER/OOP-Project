from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.trucks.trucks import Trucks
from models.constants.status import Status
from datetime import datetime, timedelta


class Route:
    _format = '%b %d %H:%Mh'
    def __init__(self, route_id: int, date_time_departure: datetime, *locations: Locations) -> None:
      
        self._route_id = route_id
        self._date_time_departure = self.format_datetime(date_time_departure)
        self._locations = locations
        self._trucks_list: list[Trucks] = []
        
        if datetime.now() < self.date_time_departure:
            self._status = Status.STANDING
        elif datetime.now() >= self.date_time_departure:
            self._status = Status.IN_PROGRESS
        elif len(self._trucks_list) == 0:
            self._status = Status.FINISHED

       
    @property
    def route_id(self):
        return self._route_id  
    
    @property
    def locations(self):
        return self._locations

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self):
        if datetime.now() < self.date_time_departure:
            self._status = Status.STANDING
        elif datetime.now() >= self.date_time_departure:
            self._status = Status.IN_PROGRESS
        elif len(self._trucks_list) == 0:
            self._status = Status.FINISHED

    @property
    def date_time_departure(self):
        return self._date_time_departure
  
    def format_datetime(self, input_datetime: str) -> datetime:
        parsed_datetime = datetime.strptime(input_datetime, "%Y%m%dT%H%M") 

        return parsed_datetime
    
    def calc_distance_time(self):
        
        date_time_departure_str = self._date_time_departure.strftime("%b %d %H:%Mh")
        route_str = f"{self._locations[0]} ({date_time_departure_str})"
        current_time = self._date_time_departure
        total_distance = 0

        for i in range(len(self._locations)-1):
            current_location = self.locations[i]
            next_location = self.locations[i+1]
            distance = getattr(Locations, current_location.lower())[next_location]
            total_distance += distance

            time_delta_hours = distance / 87 
            arrival_time = current_time + timedelta(hours=time_delta_hours)
            arrival_str = arrival_time.strftime("%b %d %H:%Mh")
            route_str += f" → {self.locations[i+1]} ({arrival_str})"
            current_time = arrival_time

        return route_str, total_distance

    def calc_current_location(self):
        time_elapsed = datetime.now() - self._date_time_departure
        km_traveled = 87 * time_elapsed.total_seconds() / 3600
        total_distance = 0
        for i in range(len(self._locations)-1):
            current_location = self.locations[i]
            next_location = self.locations[i+1]
            distance = getattr(Locations, current_location.lower())[next_location]
            total_distance += distance

            if km_traveled < total_distance:
                return f'{round(distance - km_traveled)} till {next_location}'

    def __str__(self) -> str: 
        route_str, total_distance = self.calc_distance_time() 
        current_location = self.calc_current_location()

        return f'{route_str}\nTotal distance: {total_distance}\nCurrent locations: {current_location}'           