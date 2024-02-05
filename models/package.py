from errors.application_error import ApplicationError
from models.status import PackageStatus
from models.constants.locations import Locations
class Package:
    def __init__(self, package_id: int, start_location: Locations, end_location: Locations, package_weight: int, contact_customer: str) -> None:
        self._package_id = package_id
        self._start_location = start_location
        self._end_location = end_location
        self._package_weight = package_weight
        self._contact_customer = contact_customer
        self._status = PackageStatus.CREATED

    @property
    def package_id(self):
        return self._package_id
    
    @property
    def start_location(self):
        return self._start_location
    
    @property
    def end_location(self):
        return self._end_location
    
    @property
    def package_weight(self):
        return self._package_weight
    
    @property
    def contact_customer(self):
        return self._contact_customer
    
    def __str__(self) -> str:
        pass