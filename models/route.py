from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.trucks.trucks import Trucks
from models.constants.status import Status
from datetime import datetime, timedelta
from models.package import Package


class Route:
    _format = '%b %d %H:%Mh'
    def __init__(self, route_id: int, date_time_departure: datetime, *locations: Locations) -> None:
      
        self._route_id = route_id
        self._date_time_departure = self.format_datetime(date_time_departure)
        self._locations = locations
        self.truck = None
        self._status = Status.IN_PROGRESS
        self._locations_info, self.weight_in_locations = self.stops_info()
    
        
        #if datetime.now() < self.date_time_departure:
        #    self._status = Status.STANDING
        #elif datetime.now() >= self.date_time_departure:
        #    self._status = Status.IN_PROGRESS
        #elif datetime.now() >= self.date_time_departure:
          #  self._status = Status.FINISHED

       
    @property
    def route_id(self):
        return self._route_id  
    
    @property
    def locations(self):
        return self._locations

    @property
    def status(self):
        return self._status
    
    #@status.setter
    #def status(self):
    #    if datetime.now() < self.date_time_departure:
    #        self._status = Status.STANDING
    #    elif datetime.now() >= self.date_time_departure:
    #        self._status = Status.IN_PROGRESS
    #    elif len(self.truck) == 0:
    #        self._status = Status.FINISHED

    @property
    def date_time_departure(self):
        return self._date_time_departure
    
    @property
    def truck(self):
        return self._truck
    
    @truck.setter 
    def truck(self, value):
        if value == None:
            self._truck = value
        
        else:
            if self.truck == None:
                self._truck = value
            else:
                raise ApplicationError('Truck is already assign to this route!')    
  
    def format_datetime(self, input_datetime: str) -> datetime:
        parsed_datetime = datetime.strptime(input_datetime, "%Y%m%dT%H%M") 

        return parsed_datetime
    
    def add_truck(self, truck):
        route, distance = self.calc_distance_time()
        if truck.max_range < distance:
            raise ApplicationError(f'The distance is too high for truck {truck.name}!')
        self.truck = truck
        return self.truck
    

    def calculate_travel_time(self, stop, next_stop):
        average_speed = 87
        distance = getattr(Locations, stop.lower())[next_stop]
        travel_time_hours = distance / average_speed

        return travel_time_hours
    
    
    def stops_info(self):
        #start_time, *locations = input_data.split()
        #start_time_parsed = datetime.strptime(start_time, "%Y%m%dT%H%M") 
    
        info = {self.locations[0]: self._date_time_departure}
        weight_in_stops = {self.locations[0]: 0}
        datetime_departute = self.date_time_departure
    
        for i in range(len(self.locations) - 1):
            stop = self.locations[i]
            next_stop = self.locations[i + 1]
            travel_time_hours = self.calculate_travel_time(stop, next_stop)
            datetime_departute += timedelta(hours=travel_time_hours)
            info[next_stop] = datetime_departute
            weight_in_stops[next_stop] = 0
    
        return info, weight_in_stops

    def generate_route_string(self):
        route_string = ''
        #stops = self.stops_info()
        for i, j in self._locations_info.items():
            string = f'{i} ({j.strftime("%b %dth %H:%Mh")}) → '
            route_string += string

        route_string = route_string[:-3]
        
        return route_string


    def calc_current_locations(self):
        #stops = self.stops_info()
        now = datetime.now()

        if now < list(self._locations_info.values())[0]:
            return f'Still in local hub: {list(self._locations_info.keys())[0]}'

        elif now > list(self._locations_info.values())[-1]:
            return f'Reached end location: {list(self._locations_info.keys())[-1]}'

        else:
            for k, v in self._locations_info.items():
                if now < v:  
                    time_to_next_stop = (v - now)
                    distance_to_next_stop = round(time_to_next_stop.total_seconds() / 3600 * 87)
                    return f'{distance_to_next_stop} km till {k}'

    def update_weight_in_stops(self, package : Package):
        
        self.weight_in_locations[package.start_location] += package.package_weight
        self.weight_in_locations[package.end_location] -= package.package_weight

        
    
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
        route_string = self.generate_route_string()
        calc_current_location = self.calc_current_locations()

        return f'Route #{self._route_id}\n{route_string}\nTotal distance: {total_distance}\nCurrent locations: {calc_current_location}'           