from errors.application_error import ApplicationError
from models.constants.status import Status
from models.constants.locations import Locations
from models.customer import Customer
from datetime import datetime
from models.constants.status import Status
from models.constants.package_status import PackageStatus


class Package:
    _format = '%b %d %H:%Mh'
    def __init__(self, package_id: int, start_location: Locations, end_location: Locations, package_weight: float, contact_customer: Customer) -> None:

        self._package_id = package_id
        self._start_location = start_location
        self._end_location = end_location
        self.package_weight = package_weight
        self._contact_customer = contact_customer
        self._status = Status.STANDING
        self._package_status = PackageStatus.UNASSIGN
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
    
    @package_weight.setter
    def package_weight(self, value):
        if value <= 0 :
            raise ApplicationError('The weight must be higher than 0!')
        
        self._package_weight = value
    
    @property
    def contact_customer(self):
        return self._contact_customer
    
    @property
    def time_of_creating(self):
        return self._time_of_creating
    
    @property
    def package_status(self):
        return self._package_status
    
    def current_location(self):
        if self._status == Status.STANDING:
            current_location = self._start_location.city
        elif self._status == Status.FINISHED:
            current_location = self._end_location.city
        # else:
            # for route in .all_routes_list:
            #     if route._status == Status.IN_PROGRESS:
            #         for truck in route:
            #             for pack in truck._packages:
            #                 if self._package_id == pack._package_id:
            #                     current_location = route.calc_current_location()

        return current_location
    
    
    def __str__(self) -> str:
        return f'''Package: #{self.package_id}
Created on: {self.time_of_creating.strftime(Package._format)}
From: {self._start_location.city}
To: {self._end_location.city}
Weight: {self._package_weight}
Status: {self._status}{self._status}
Curren location: {str(self.current_location())}'''