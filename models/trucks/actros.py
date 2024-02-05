from models.constants.name import Name
from models.trucks.trucks import Trucks
class Actros(Trucks):

        
    CAPACITY = 26000
    MAX_RANGE = 13000
    NUMBER_OF_TRUCKS = 15

    def __init__(self, truck_id: int, name: str, capacity: float, max_range: int, num_of_trucks: int):
        super().__init__(truck_id, name, capacity, max_range, num_of_trucks)

        self.name = Name.ACTROS
        self._capacity = Actros.CAPACITY
        self._max_range = Actros.MAX_RANGE
        self._num_of_trucks = Actros.NUMBER_OF_TRUCKS

   