from models.constants.name import Name
from models.trucks.trucks import Trucks
class Man(Trucks):
        
    CAPACITY = 37000
    MAX_RANGE = 10000
    NUMBER_OF_TRUCKS = 15

    def __init__(self, truck_id: int, name: str, capacity: float, max_range: int, num_of_trucks: int):
        super().__init__(truck_id, name, capacity, max_range, num_of_trucks)
        
        self.name = Name.MAN
        self._capacity = Man.CAPACITY
        self._max_range = Man.MAX_RANGE
        self._num_of_trucks = Man.NUMBER_OF_TRUCKS