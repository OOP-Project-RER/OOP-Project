from models.constants.name import Name
from models.trucks.trucks import Trucks
from errors.application_error import ApplicationError

class Man(Trucks):
        
    CAPACITY = 37000
    MAX_RANGE = 10000
    NUMBER_OF_TRUCKS = 15
    _man_id = 1011

    def __init__(self, name: Name, truck_id: int = 0, capacity: float = CAPACITY, max_range: int = MAX_RANGE, num_of_trucks: int = NUMBER_OF_TRUCKS):
        super().__init__(truck_id, name, capacity, max_range, num_of_trucks)
        
        self.name = Name.from_string(name)
        self.truck_id = Man._man_id
        Man._man_id += 1

    @property
    def truck_id(self):
        return self._truck_id
    
    @truck_id.setter
    def truck_id(self, value):
        if value > 1025:
                raise ApplicationError('You don\'t have any more Man trucks')
        self._truck_id = value
