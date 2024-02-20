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
        self._date_time_departure = date_time_departure #self.date_time_departure = date_time_departure 
        self._locations = locations
        self.truck = None
        self._status = datetime.now()  
        self._stops_date_time, self.weight_in_locations = self.stops_info()
        self._total_distance = self.calc_total_distance()
    
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
    def status(self, date_time : datetime):
        '''Take datetime as parameter and depends on the day change the status'''
        if date_time < self.date_time_departure:
            self._status = Status.STANDING
            
        elif date_time >= self.date_time_departure and date_time < self._stops_date_time[self.locations[-1]]:
                self._status = Status.IN_PROGRESS

        else:
            self._status = Status.FINISHED

    @property
    def date_time_departure(self):
        return self._date_time_departure
    
    #@date_time_departure.setter
    #def date_time_departure(self, input_datetime: str) -> datetime:
    '''Restrict you to make route in the past and takes at least 1 hour from the moment on the creating the route'''
    #    #parsed time = datetime.strptime(input_datetime, "%Y%m%dT%H%M")
    #    
    #    if datetime.now() > input_datetime:
    #        raise ApplicationError(f'You can\'t create route in the past time')
    #    
    #    elif datetime.now() + timedelta(hours = 1) > input_datetime:
    #        raise ApplicationError(F'It takes at least 1 hour to prepare to truck for departure') 
    #    
    #    self._date_time_departure = input_datetime


        
    @property
    def truck(self):
        return self._truck
    
    @truck.setter 
    def truck(self, value):
        '''Restrict you from assigning 2 trucks for 1 route'''
        if value == None:
            self._truck = value
        
        else:
            if self.truck == None:
                self._truck = value
            else:
                raise ApplicationError('Truck is already assign to this route!')

    @property
    def total_distance(self):
        return self._total_distance    
     
    def add_truck(self, truck:Trucks) -> Trucks:
        '''Check if the distance is not higher than the truck range before adding the truck for route'''
        if truck.max_range < self.total_distance:
            raise ApplicationError(f'The distance is too high for truck {truck.name}!')
        self.truck = truck

        return self.truck 

    def calculate_travel_time(self, stop:Locations, next_stop:Locations) -> float:
        '''Calculate the time to travel certain distance'''
        average_speed = 87
        distance = getattr(Locations, stop.lower())[next_stop]
        travel_time_hours = distance / average_speed

        return travel_time_hours
    
    
    def stops_info(self) -> dict:
        ''' Create 2 dict with keys every stop of the route. 
        First dict is holding as values the time of arriving 
        Second dict is holding as values the weight that is adding or removing from the truck on every stop'''

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

    def generate_route_string(self) -> str:
        '''Generate string with information for every stop arriving time'''
        route_string = ''
        
        for i, j in self._stops_date_time.items():
            string = f'{i} ({j.strftime("%b %d %H:%Mh")}) → '
            route_string += string

        route_string = route_string[:-3]
        
        return route_string

    def calc_current_locations(self) -> str:
        '''Return string with information for the current location of the route'''
        
        now = datetime.now()

        if now < list(self._stops_date_time.values())[0]:
            return f'Still in local hub: {list(self._stops_date_time.keys())[0]}'

        elif now > list(self._stops_date_time.values())[-1]:
            return f'Reached end location: {list(self._stops_date_time.keys())[-1]}'

        else:
            for k, v in self._stops_date_time.items():
                if now < v:  
                    time_to_next_stop = (v - now)
                    distance_to_next_stop = round(time_to_next_stop.total_seconds() / 3600 * 87)
                    return f'{distance_to_next_stop} km till {k}'

    def update_weight_in_stops(self, package : Package):
        '''Updating dict for weight in every stop'''
        
        self.weight_in_locations[package.start_location] += package.package_weight
        self.weight_in_locations[package.end_location] -= package.package_weight

    def remove_package(self, package : Package):
        '''Remove package from the route and upgrade the weight in every stop'''
        package._departure_time = None
        package._arriving_time = None
        self.weight_in_locations[package.start_location] -= package.package_weight
        self.weight_in_locations[package.end_location] += package.package_weight

    def calc_total_distance(self) -> int:
        '''Calculate the total distance for the route'''
        total_distance = 0
        for i in range(len(self._locations)-1):
            current_location = self.locations[i]
            next_location = self.locations[i+1]
            distance = getattr(Locations, current_location.lower())[next_location]
            total_distance += distance

        return total_distance

    def __str__(self) -> str: 
        '''Generate string with route ID, total distance and current location'''
        route_string = self.generate_route_string()
        calc_current_location = self.calc_current_locations()

        return f'Route #{self._route_id}\n{route_string}\nTotal distance: {self._total_distance}\nCurrent locations: {calc_current_location}'           