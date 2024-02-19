from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.constants.status import Status
from models.employee import Employee
from models.route import Route
from models.trucks.trucks import Trucks
from models.package import Package
from models.trucks.scania import Scania
from models.trucks.man import Man
from models.trucks.actros import Actros
from datetime import datetime, timedelta
from models.constants.encoder import Encoder
import json



class ApplicationData:
    def __init__(self):
        '''Initialize a object'''
        self._employees = []
        self._logged_employee = None
        self._all_packages_list: list[Package] = []
        self._all_routes_list: list[Route] = []
        self._all_trucks ={'Scania':[(Scania('Scania')) for i in range(10)], 
                        'Man': [(Man('Man')) for l in range(15)],
                        'Actros': [(Actros('Actros')) for l in range(15)]}
        self._file_path = "save_application_data.json"


    @property
    def employees(self):
        return tuple(self._employees)
    
    @property
    def all_packages_list(self):
        return tuple(self._all_packages_list)
    
    @property
    def all_routes_list(self):
        return self._all_routes_list
    
    @property
    def all_trucks(self):
        return self._all_trucks
    
    def save_to_json(self):
        ''' Creates dictionary that saving data'''
        data = {
                "employees": [emp.__dict__ for emp in self._employees],
                "logged_employee": self._logged_employee.__dict__ if self._logged_employee else None,
                "all_packages_list": [package.__dict__ for package in self._all_packages_list],
                "all_routes_list": [route.__dict__ for route in self._all_routes_list]
            }
        try:
            with open('save_application_data.json', 'w') as file:
                json.dump(data, file, indent=4, cls=Encoder)
        except Exception as e:
            print(f"Error saving data to file: {e}")


    def create_employee(self, username:str, firstname:str, lastname:str, password:int, user_role) -> Employee:
        '''Creates object of class Employee'''
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ApplicationError(
                f'User {username} already exist. Choose a different username!')

        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)

        return employee
    
    def find_employee_by_username(self, username: str) -> Employee:
        '''Finding employee from list by username'''
        filtered = [employee for employee in self._employees if employee.username == username]
        if filtered == []:
            raise ApplicationError(f'There is no employee with username {username}!')

        return filtered[0]
    
    @property
    def logged_in_employee(self):
    
        if self.has_logged_in_employee:
            return self._logged_employee
        else:
            raise ApplicationError('There is no logged in employee.')

    @property
    def has_logged_in_employee(self):
        return self._logged_employee is not None

    def login(self, employee: Employee):
        '''Assign value of Employee object to attribute'''
        self._logged_employee = employee

    def logout(self):
        '''Chanage the value of attribute with None'''
        self._logged_employee = None

    def add_package(self, package: Package):
        ''' Add object of class Package to list'''
        if not any(p._package_id == package._package_id for p in self._all_packages_list):
            self._all_packages_list.append(package)
            self.save_to_json()

    def add_route(self, route: Route):
        '''Add object of class Route to list'''
        if not any(r._route_id == route._route_id for r in self._all_routes_list):
            self._all_routes_list.append(route)
            self.save_to_json()
            
    def find_package_by_id(self, id:int) -> Package:
        '''Find object of class Package by id and return this object'''
        package = [pac for pac in self.all_packages_list if id == pac.package_id]
        if package == []:
            raise ApplicationError(f'Package with ID: {id} can\'t be find!')
        
        return package[0]
    
    def find_route_by_id(self, id:int) -> Route:
        '''Find object of class Route by id and return this object'''
        route = [rt for rt in self.all_routes_list if id ==rt.route_id]
        if route == []:
            raise ApplicationError(f'Route with ID: {id} can\'t be find!') 
        
        return route[0]
    
    def find_truck_by_id(self, id:int) -> Trucks:
        '''Find object of class Trucks by id and return this object'''
        truck = [truck for trucks in self.all_trucks.values() for truck in trucks if id == truck.truck_id] 

        if truck == []:
            raise ApplicationError(f'Truck with ID: {id} can\'t be find!')
        
        return truck[0]
    
    def parsed(self, input_datetime: str) -> datetime:
        '''Parsing string value to datetime of certain format'''
        try:
            parsed_datetime = datetime.strptime(input_datetime, "%Y%m%dT%H%M")
        except:
            raise ApplicationError('Invalid format for date/time! Should be yyyymmddThhmm (20240219T1000)')

        return parsed_datetime
    
    def check_if_route_can_be_assign_to_truck(self, route:Route, truck:Trucks):
        '''Checks if certain route can fit in the schedule of certain truck'''
        
        routes_end_time_before_departure_of_route = filter(lambda x: x._stops_date_time[x.locations[-1]] < route.date_time_departure,                                                   
                                                           truck._routes_list)
        
        before_departure = sorted(routes_end_time_before_departure_of_route, 
                               key=lambda x: x._stops_date_time[x.locations[-1]],reverse=True)
        
        if len(before_departure) > 0:
            start_location, end_location = before_departure[0].locations[-1],route.locations[0]
            
            travel_time_hours = route.calculate_travel_time(start_location, end_location)
            
            if before_departure[0]._stops_date_time[start_location] + timedelta(hours = travel_time_hours) > route.date_time_departure:
                raise ApplicationError(f'This truck can\'t get back on time for this route!')
            
        
        routes_departure_time_after_end_of_route = filter(lambda x: x.date_time_departure > route._stops_date_time[route.locations[-1]],
                                                          truck._routes_list)
        
        after_arrival = sorted(routes_departure_time_after_end_of_route, 
                               key=lambda x: x.date_time_departure)
        
        if len(after_arrival) > 0:
            start_location, end_location = route.locations[-1], after_arrival[0].locations[0]
        
            travel_time_hours = route.calculate_travel_time(start_location, end_location)

            if route._stops_date_time[start_location] + timedelta(hours = travel_time_hours) > after_arrival[0].date_time_departure:
                raise ApplicationError(f'This truck won\'t be able get back on time for next route that is already scheduled!')

        
        truck_schedules = [rt for rt in truck._routes_list 
                           if rt.status != Status.FINISHED and 
                           route.date_time_departure < rt._stops_date_time[rt.locations[-1]]]

        if True in [True for rt in truck_schedules if route._stops_date_time[route.locations[-1]] > rt.date_time_departure]:
            raise ApplicationError('The route can\'t be assign to this truck. Different route is scheduled for this truck!')

    def check_if_package_locations_are_in_route_locations(self, package:Package, route:Route):
        '''Checks if package's locations are in route's locations'''
        if package.start_location not in route.locations or package.end_location not in route.locations:
            raise ApplicationError('One or both of the locations in package doesn\'t match the route locations!')
        
        if datetime.now() > route._stops_date_time[package.start_location]:
            raise ApplicationError(f'The truck already passed {package.start_location}')
        
    def check_if_package_weight_can_be_adde_to_route(self, package:Package, route:Route):
        '''Check if package can be added to route'''
        end_index = route.locations.index(package.end_location)
        capacity_at_stop = 0

        for i in range(end_index):
            capacity_at_stop += route.weight_in_locations[route.locations[i]]
        
        if (capacity_at_stop + package.package_weight) > route.truck.capacity:
            raise ApplicationError(f'Can\'t assign package #{package._package_id} to route #{route.route_id}. The weight is too much!')

    
    def check_for_route(self, start_location: str, end_location: str) -> Locations:
        '''Check if routes's schedule are passing throw 2 locations'''
        found_routes = []
        for route in self.all_routes_list:
            if route.status != Status.FINISHED:
                if start_location in route.locations and end_location in route.locations:
                    start_index = route.locations.index(start_location)
                    end_index = route.locations.index(end_location)
                    if start_index < end_index:
                        found_routes.append(route)
        
        if len(found_routes) > 0:
            routes = []
            for i in found_routes:
                route_str = i.generate_route_string()
                routes.append(route_str)
            return routes

        return [f"There is not a route from {start_location} to {end_location}"]
        
        