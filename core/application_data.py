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
from datetime import datetime


class ApplicationData:
    def __init__(self):
        self._employees = []
        self._logged_employee = None
        self._all_packages_list: list[Package] = []
        self._all_routes_list: list[Route] = []
        self._all_trucks ={'Scania':[(Scania('Scania')) for i in range(10)], 
                        'Man': [(Man('Man')) for l in range(15)],
                        'Actros': [(Actros('Actros')) for l in range(15)]}


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
        return tuple(self._all_trucks)

    def create_employee(self, username:str, firstname:str, lastname:str, password:int, user_role) -> Employee:
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ApplicationError(
                f'User {username} already exist. Choose a different username!')

        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)

        return employee
    
    def find_employee_by_username(self, username: str) -> Employee:
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
        self._logged_employee = employee

    def logout(self):
        self._logged_employee = None

    def add_package(self, package: Package):
        if not any(p._package_id == package._package_id for p in self._all_packages_list):
            self._all_packages_list.append(package)

    def add_route(self, route: Route):
        if not any(r._route_id == route._route_id for r in self._all_routes_list):
            self._all_routes_list.append(route)

    def find_package_by_id(self, id:int) -> Package:
        package = [pac for pac in self.all_packages_list if id == pac.package_id]
        if package == []:
            raise ApplicationError(f'Package with ID: {id} can\'t be find!')
        
        return package[0]
    
    def find_route_by_id(self, id:int) -> Route:
        route = [rt for rt in self.all_routes_list if id ==rt.route_id]
        if route == []:
            raise ApplicationError(f'Route with ID: {id} can\'t be find!') 
        
        return route[0]
    
    def check_if_route_can_be_assign_to_truck(self, route:Route, truck:Trucks):
        truck_schedules = [rt for rt in truck._routes_list 
                           if rt.status != Status.FINISHED and 
                           route.date_time_departure < rt._locations_info[rt.locations[-1]]]

        if True in [True for rt in truck_schedules if route._locations_info[route.locations[-1]] > rt.date_time_departure]:
            raise ApplicationError('The route can\'t be assign to this truck. Different route is scheduled for this truck!')

    def check_if_package_locations_are_in_route_locations(self, package:Package, route:Route):
        if package.start_location not in route.locations or package.end_location not in route.locations:
            raise ApplicationError('One or both of the locations in package doesn\'t match the route locations!')
        
        if datetime.now() > route._locations_info[package.start_location]:
            raise ApplicationError(f'The truck already passed {package.start_location}')
        
    def check_if_package_is_already_added(self, package:Package, route:Route):
        if True in [True for pack in route.truck.packages if pack.package_id == package.package_id]:
            raise ApplicationError(f'Package #{package.package_id} is already added to this route!')
    
    def check_if_package_weight_can_be_adde_to_route(self, package:Package, route:Route):
        end_index = route.locations.index(package.end_location)
        capacity_at_stop = 0

        for i in range(end_index):
            capacity_at_stop += route.weight_in_locations[route.locations[i]]
        
        if (capacity_at_stop + package.package_weight) > route.truck.capacity:
            raise ApplicationError(f'Can\'t assign package #{package._package_id} to route #{route.route_id}. The weight is too much!')

    
    def check_for_route(self, start_location: str, end_location: str) -> Locations:
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
        
        