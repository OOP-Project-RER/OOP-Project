from errors.application_error import ApplicationError
from models.package import Package
from models.route import Route
from models.constants.locations import Locations
from models.customer import Customer
from datetime import datetime
import json

class ModelsFactory:
    def __init__(self):
        self._package_id = 1
        self._route_id = 101
        self._file_path = "models_factory.json"


    def _save_last_package_and_route_id_to_json(self):
        '''Create dictinary and save data for routes and packages'''
        data = {
            "package_id": self._package_id,
            "route_id": self._route_id
        }
        with open(self._file_path, "w") as file:
            json.dump(data, file)


    def create_package(self, start_location: Locations, end_location: Locations, package_weight: float, contact_customer: Customer):
        '''Create object of class Package'''
        
        with open(self._file_path, "r") as file:
            data = json.load(file)
            self._package_id = data["package_id"]

        self._route_id = data["route_id"]
        package_id = self._package_id
        self._package_id += 1

        self._save_last_package_and_route_id_to_json()

        return Package(package_id, start_location, end_location, package_weight, contact_customer)

    def create_route(self, date_time_departure: datetime,*other_locations: Locations):
        '''Create object of class Route'''
        route_id = self._route_id
        self._route_id +=1
        self._save_last_package_and_route_id_to_json()

        return Route(route_id, date_time_departure, *other_locations)