from models.package import Package
class Trucks:
    def __init__(self, truck_id: int, name: str, capacity: float, max_range: int, num_of_trucks: int):
        self.truck_id = truck_id
        self.name = name
        self._capacity = capacity
        self._max_range = max_range
        self._num_of_trucks = num_of_trucks
        self._packages: list[Package] = []
        
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def max_range(self):
        return self._max_range
    
    @property
    def num_of_trucks(self):
        return self._num_of_trucks
    
    @property
    def packages(self):
        return tuple(self._packages)