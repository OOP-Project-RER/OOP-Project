from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.constants.status import Status
from models.constants.name import Name
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
        if len(self.params) == 2:
            vehicle_str, id = self.params
            vehicle = Name.from_string(vehicle_str)
            id = self._try_parse_int(self.params[1])
            route = self._app_data.find_route_by_id(id)

            #To Do 
            #city = route.locations[0]
            #city_trucks = Locations.city_trucks.get(city)

            #if city_trucks.get(vehicle) == 0:
            #aise ApplicationError(f'Truck {vehicle} is not available in {city} hub')
            #else:
            trucks = [truck for truck in self.app_data.all_trucks[vehicle]]  #if truck.status == Status.STANDING
        
            for i in range(len(trucks)):
                try:
                    self._app_data.check_if_route_can_be_assign_to_truck(route, trucks[i])
                    truck = trucks[i]  
                    break
            
                except:
                    if i == len(trucks)-1:
                        raise ApplicationError(f'There is no available {vehicle} truck at the moment!')
                    pass
        else:
            vehicle_str, id_tr, id_rt = self.params
            vehicle = Name.from_string(vehicle_str)
            id_truck = self._try_parse_int(id_tr)
            id_route = self._try_parse_int(id_rt)

            route = self._app_data.find_route_by_id(id_route)

            trucks = [truck for truck in self.app_data.all_trucks[vehicle] if id_truck == truck.truck_id]
            if trucks == []:
                raise ValueError(f'There is no {vehicle} with that ID')
            
            truck = trucks[0]
            self._app_data.check_if_route_can_be_assign_to_truck(route, truck)


        
        route.add_truck(truck)
        truck.add_route(route)
 
        #city_trucks[vehicle] -= 1
            
        return f'Truk {vehicle} with ID:{truck.truck_id} was assigned to route #{route.route_id}'

    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [2,3]
        