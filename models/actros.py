from models.constants.make import Make
class Actros: # Create base class Trucks

        
    CAPACITY = 26000
    MAX_RANGE = 13000
    NUMBER_OF_TRUCKS = 15

    def __init__(self):
        self.name = Make.ACTROS
        self.capacity = Actros.CAPACITY
        self.max_range = Actros.MAX_RANGE
        self.num_of_trucks = Actros.MAX_RANGE
