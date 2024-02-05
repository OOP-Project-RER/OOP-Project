from models.constants.make import Make
class Man:
        
    CAPACITY = 37000
    MAX_RANGE = 10000
    NUMBER_OF_TRUCKS = 15

    def __init__(self):
        self.name = Make.MAN
        self.capacity = Man.CAPACITY
        self.max_range = Man.MAX_RANGE
        self.num_of_trucks = Man.MAX_RANGE
