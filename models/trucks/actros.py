from models.constants.name import Name
from models.trucks.trucks import Trucks
class Actros(Trucks):

        
    CAPACITY = 26000
    MAX_RANGE = 13000
    NUMBER_OF_TRUCKS = 15

    def __init__(self, name: str, capacity: int, max_range: int, num_of_trucks: int):
        super().__init__(name, capacity, max_range, num_of_trucks)

        self.name = Name.ACTROS
        self._capacity = Actros.CAPACITY
        self._max_range = Actros.MAX_RANGE
        self._num_of_trucks = Actros.NUMBER_OF_TRUCKS

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def max_range(self):
        return self._max_range
    
    @property
    def num_of_trucks(self):
        return self._num_of_trucks