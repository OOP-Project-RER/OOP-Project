from models.constants.name import Name
from models.trucks.trucks import Trucks
from errors.application_error import ApplicationError

class Actros(Trucks):
        
    CAPACITY = 26000
    MAX_RANGE = 13000
    NUMBER_OF_TRUCKS = 15
    _actros_id = 1026

    def __init__(self, name: Name, truck_id: int = 0, capacity: float = CAPACITY, max_range: int = MAX_RANGE, num_of_trucks: int = NUMBER_OF_TRUCKS):
        super().__init__(truck_id, name, capacity, max_range, num_of_trucks)

        self.name = Name.from_string(name)
        self.truck_id = Actros._actros_id
        Actros._actros_id += 1

    @property
    def truck_id(self):
        return self._truck_id
    
    @truck_id.setter
    def truck_id(self, value):
        '''Restrict the value donot go above 1040'''
        if value > 1040:
                raise ApplicationError('You don\'t have any more Actros trucks')
        self._truck_id = value