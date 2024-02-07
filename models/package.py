from errors.application_error import ApplicationError
from models.constants.status import Status
from models.constants.locations import Locations
from models.customer import Customer
from datetime import datetime


class Package:
    _format = '%d/%m/%Y, %H:%M:%S'
    def __init__(self, package_id: int, start_location: Locations, end_location: Locations, package_weight: float, contact_customer: Customer) -> None:
        
        if package_weight <= 0:
            raise ApplicationError('Invalid value for package_weight!')

        self._package_id = package_id
        self._start_location = start_location
        self._end_location = end_location
        self._package_weight = package_weight
        self._contact_customer = contact_customer
        self._status = Status.STANDING
        self._time_of_creating = datetime.now()


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
    
    @property
    def time_of_creating(self):
        return self._time_of_creating
    
    
    def __str__(self) -> str:
        return f'''Package: #{self.package_id}
Created on: {self.time_of_creating.strftime(Package._format)}
From: {self._start_location.city}
To: {self._end_location.city}
Weight: {self._package_weight}
Status: {self._status}'''