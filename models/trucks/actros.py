from models.constants.name import Name
from models.trucks.trucks import Trucks
class Actros(Trucks):

        
    CAPACITY = 26000
    MAX_RANGE = 13000
    NUMBER_OF_TRUCKS = 15

    def __init__(self, name: str, capacity: int, max_range: int, num_of_trucks: int):
        super().__init__(name, capacity, max_range, num_of_trucks)

        self.name = Name.ACTROS
        self.capacity = Actros.CAPACITY
        self.max_range = Actros.MAX_RANGE
        self.num_of_trucks = Actros.NUMBER_OF_TRUCKS
