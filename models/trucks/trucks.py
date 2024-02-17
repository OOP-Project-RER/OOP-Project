from errors.application_error import ApplicationError
from models.package import Package
#from models.route import Route
from models.constants.status import Status



class Trucks:
    def __init__(self, truck_id: int, name: str,  capacity: float=0, max_range: int=0, num_of_trucks: int=0):
        self._truck_id = truck_id
        self.name = name
        self._capacity = capacity
        self._max_range = max_range
        self._num_of_trucks = num_of_trucks
        self._routes_list: list  = []
        self._packages: list[Package] = []
        self._status = Status.STANDING

    @property
    def truck_id(self):
        return self._truck_id

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
    
    @property
    def status(self):
        return self._status

    def add_package(self, package: Package):
        self._packages.append(package)

    def add_route(self, route):
        self._routes_list.append(route)

    def view(self):
        return '\n'.join([f'{self}'] + [f'  {package}' for package in self.packages])

    def __str__(self):
        return f'#{self.truck_id}. {self.name} ({len(self.packages)} packages)'    