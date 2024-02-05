from models.constants.name import Name
from models.trucks.trucks import Trucks
class Scania(Trucks):
        
    CAPACITY = 42000
    MAX_RANGE = 8000
    NUMBER_OF_TRUCKS = 10

    def __init__(self, name: str, capacity: int, max_range: int, num_of_trucks: int):
        super().__init__(name, capacity, max_range, num_of_trucks)
        
        self.name = Name.SCANIA
        self.capacity = Scania.CAPACITY
        self.max_range = Scania.MAX_RANGE
        self.num_of_trucks = Scania.NUMBER_OF_TRUCKS
