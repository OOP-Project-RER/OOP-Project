from errors.application_error import ApplicationError
from models.package import Package
from models.route import Route
from models.constants.locations import Locations
from models.customer import Customer
from models.constants.name import Name
from models.trucks.trucks import Trucks

class ModelsFactory:
    def __init__(self):
        self._package_id = 1
        self._truck_id = 1 
        self._route_id = 1

    def create_package(self, start_location: Locations, end_location: Locations, package_weight: float, contact_customer: Customer):
        package_id = self._package_id
        self._package_id += 1

        return Package(package_id, start_location, end_location, package_weight, contact_customer)
    
    def create_truck(self, name: Name, capacity: float,	max_range: int,	num_of_trucks: int):
        if name == Name.SCANIA:
            self._truck_id = 1001
            truck_id = self._truck_id
            self._truck_id += 1

            return Trucks(truck_id, name, capacity, max_range, num_of_trucks)

        if name == Name.MAN:
            self._truck_id = 1011
            truck_id = self._truck_id
            self._truck_id += 1

            return Trucks(truck_id, name, capacity, max_range, num_of_trucks)

        if name == Name.ACTROS:
            self._truck_id = 1026
            truck_id = self._truck_id
            self._truck_id += 1

            return Trucks(truck_id, name, capacity, max_range, num_of_trucks)


    def create_route(self, locations: list):
        route_id = self._route_id
        self._route_id +=1

        return Route(route_id, locations)