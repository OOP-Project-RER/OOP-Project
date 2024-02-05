from models.constants.make import Make
class Scania:
        
    CAPACITY = 42000
    MAX_RANGE = 8000
    NUMBER_OF_TRUCKS = 10

    def __init__(self):
        self.name = Make.SCANIA
        self.capacity = Scania.CAPACITY
        self.max_range = Scania.MAX_RANGE
        self.num_of_trucks = Scania.MAX_RANGE
