from models.constants.locations import Locations
from models.constants.status import Status
from models.employee import Employee
from models.route import Route
from models.trucks.trucks import Trucks
from models.package import Package


class ApplicationData:
    def __init__(self):
        self._employees = []
        self._logged_employee = None
        self._all_packages_list: list[Package] = []
        self._all_routes_list: list[Route] = []


    @property
    def employees(self):
        return tuple(self._employees)
    
    @property
    def all_packages_list(self):
        return tuple(self._all_packages_list)
    
    @property
    def all_routes_list(self):
        return tuple(self._all_routes_list)

    def create_employee(self, username, firstname, lastname, password, user_role) -> Employee:
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ValueError(
                f'User {username} already exist. Choose a different username!')

        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)

        return employee
    
    def find_employee_by_username(self, username: str) -> Employee:
        filtered = [employee for employee in self._employees if employee.username == username]
        if filtered == []:
            raise ValueError(f'There is no employee with username {username}!')

        return filtered[0]
    
    @property
    def logged_in_employee(self):
        if self.has_logged_in_employee:
            return self._logged_employee
        else:
            raise ValueError('There is no logged in employee.')

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
            raise ValueError(f'Package with ID: {id} can\'t be find!')
        
        return package[0]
    
    def find_route_by_id(self, id):
        route = [rt for rt in self.all_routes_list if id ==rt.route_id]
        if route == []:
            raise ValueError(f'Route with ID: {id} can\'t be find!') 
        
        return route[0]
    
    def check_for_route(self, start_location: str, end_location: str) -> Locations:
        found_routes = []
        for route in self.all_routes_list:
            if route.status == Status.STANDING or route.status == Status.IN_PROGRESS:
                if start_location in route.locations and end_location in route.locations:
                    start_index = route.locations.index(start_location)
                    end_index = route.locations.index(end_location)
                if start_index < end_index:
                    found_routes.append(route)
        if len(found_routes) > 0:
            routes = []
            for i in found_routes:
                route_str, total_distance = route.calc_distance_time()
                routes.append(route_str)
            return routes

        return [f"There is not a route from {start_location} to {end_location}"]
        
        