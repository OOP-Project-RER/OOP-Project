from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError
from models.constants.locations import Locations

class AssignTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory : ModelsFactory):
        self._models_factory = models_factory
        super().__init__(params, app_data)

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        #return super().execute()
        vehicle = self.params[0]
        id = self._try_parse_int(self.params[1])

        route = self._app_data.find_route_by_id(id)
        city = route.locations[0]
        city_trucks = Locations.city_trucks.get(city)
        try:
            if city_trucks.get(vehicle) == 0:
                raise ValueError(f'Truck {vehicle} is not available in {city} hub')
            else:
                truck = self.models_factory.create_truck(vehicle)
                route.add_truck(truck)
                city_trucks[vehicle] -= 1
                return f'{vehicle} with ID:{truck._truck_id} truck was assigned to route #{self.params[1]}'
        
        except Exception as e:
            print(e)

            print(truck.truck_id)
            




        