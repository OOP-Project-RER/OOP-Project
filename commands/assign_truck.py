from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.constants.status import Status
import random

class AssignTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory : ModelsFactory):
        self._models_factory = models_factory
        super().__init__(params, app_data)

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        #super().execute()

        vehicle = self.params[0]
        id = self._try_parse_int(self.params[1])

        route = self._app_data.find_route_by_id(id)
        city = route.locations[0]
        city_trucks = Locations.city_trucks.get(city)

        if city_trucks.get(vehicle) == 0:
            raise ApplicationError(f'Truck {vehicle} is not available in {city} hub')
        else:
            truck = random.choice([truck for truck in self.app_data._all_trucks[vehicle]  if truck.status == Status.STANDING])
            route.add_truck(truck)
            truck._status = Status.IN_PROGRESS
            city_trucks[vehicle] -= 1
            
            return f'Truck {vehicle} with ID:{truck.truck_id} was assigned to route #{self.params[1]}'

    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [2]
        