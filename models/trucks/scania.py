from models.constants.name import Name
from models.trucks.trucks import Trucks
from errors.application_error import ApplicationError

class Scania(Trucks):
        
    CAPACITY = 42000
    MAX_RANGE = 8000
    NUMBER_OF_TRUCKS = 10
    _scania_id = 1001

    def __init__(self, name: Name, truck_id: int = 0, capacity: float = CAPACITY, max_range: int = MAX_RANGE, num_of_trucks: int = NUMBER_OF_TRUCKS):
        super().__init__(truck_id, name, capacity, max_range, num_of_trucks)
        
        self.name = Name.from_string(name)
        self.truck_id = Scania._scania_id
        Scania._scania_id += 1

    @property
    def truck_id(self):
        return self._truck_id
    
    @truck_id.setter
    def truck_id(self, value):
        '''Restrict the value donot go above 1010'''
        if value > 1010:
            raise ApplicationError('You don\'t have any more Scania trucks')
        self._truck_id = value