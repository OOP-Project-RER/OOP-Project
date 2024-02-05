from errors.application_error import ApplicationError
from models.package import Package

class ModelsFactory:
    def __init__(self):
        self._package_id = 1
        self._truck_id = 1 # Need fixing the id. It has to be from 1001-1040 depens on the truck
        self._route_id = 1

    def create_package(self, start_location, end_location, package_weight: float, contact_customer):
        package_id = self._package_id
        self._package_id += 1

        return Package(package_id, start_location, end_location, package_weight, contact_customer)