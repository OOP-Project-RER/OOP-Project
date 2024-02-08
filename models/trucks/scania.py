from models.constants.name import Name
from models.trucks.trucks import Trucks
class Scania(Trucks):
        
    CAPACITY = 42000
    MAX_RANGE = 8000
    NUMBER_OF_TRUCKS = 10

    def __init__(self, truck_id: int, name: str, capacity: float = CAPACITY, max_range: int = MAX_RANGE, num_of_trucks: int = NUMBER_OF_TRUCKS):
        super().__init__(truck_id, name, capacity, max_range, num_of_trucks)
        
    #self.name = Name.SCANIA
    #self._capacity = Scania.CAPACITY
    #self._max_range = Scania.MAX_RANGE
    #self._num_of_trucks = Scania.NUMBER_OF_TRUCKS