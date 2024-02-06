from models.package import Package

class Trucks:
    def __init__(self, name: str, truck_id: int=0, capacity: float=0, max_range: int=0, num_of_trucks: int=0):
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
    
    def add_package(self, package: Package):
        if package.package_weight > self._capacity:
            raise ValueError("Package weight is bigger than truck capacity")
        self._capacity -= package.package_weight 
        self._packages.append(package)

    def view(self):
        return '\n'.join([f'{self}'] + [f'  {package}' for package in self.packages])

    def __str__(self):
        return f'#{self.truck_id}. {self.name} ({len(self.packages)} packages)'    