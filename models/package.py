from errors.application_error import ApplicationError
from models.constants.status import Status
from models.constants.locations import Locations
from models.customer import Customer
from datetime import datetime
from models.constants.status import Status



class Package:
    _format = '%b %d %H:%Mh'
    def __init__(self, package_id: int, start_location: Locations, end_location: Locations, package_weight: float, contact_customer: Customer) -> None:

        self._package_id = package_id
        self._start_location = start_location
        self._end_location = end_location
        self.package_weight = package_weight
        self._contact_customer = contact_customer
        self._departure_time = None
        self._arriving_time = None
        self.status = datetime.now()
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
        '''Check if value is higher than 0'''
        if value <= 0 :
            raise ApplicationError('The weight must be higher than 0!')
        
        self._package_weight = value
    
    @property
    def contact_customer(self):
        return self._contact_customer
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, date_time : datetime):
        '''Change the status based on date and time'''
        if self._departure_time == None:
            self._status = Status.UNASSIGN
        else:   
            if date_time < self._departure_time:
                self._status = Status.STANDING
            
            elif date_time >= self._departure_time and date_time < self._arriving_time:
                self._status = Status.IN_PROGRESS

            else:
                self._status = Status.FINISHED
    
    @property
    def time_of_creating(self):
        return self._time_of_creating
    
    def current_location(self):
        '''Return information where is the package based on date and time'''
        now = datetime.now()

        if now < self._departure_time:
            return f'Still in {self.start_location} hub. Waiting for the truck!'

        elif now > self._arriving_time:
            return f'Reached end location: {self.end_location}'

        else:  
            time_to_next_stop = (self._arriving_time - now)
            distance_to_next_stop = round(time_to_next_stop.total_seconds() / 3600 * 87)
            return f'{distance_to_next_stop} km till {self.end_location}'
    
    def __str__(self) -> str:
        '''Return detailed information for the package'''
        str_list = [f'Package: #{self.package_id}',
                    f'Created on: {self.time_of_creating.strftime(Package._format)}',
                    f'From: {self._start_location}',
                    f'To: {self._end_location}',
                    f'Weight: {self._package_weight}',
                    f'Status: {self._status}',
                    ]

        if self._status == Status.UNASSIGN:
            return '\n'.join(str_list) + f'\nStill in the hub. Its not assign to route, yet!'

        else: 
            return '\n'.join(str_list) + f'\nDeparture/Arriving: {self._departure_time.strftime(Package._format)} /' \
            + f'{self._arriving_time.strftime(Package._format)}' + f'\nCurrent locations: {self.current_location()}'
                    