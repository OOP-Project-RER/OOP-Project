from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from errors.application_error import ApplicationError
from models.trucks.trucks import Trucks


class AddPackToTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)


    def execute(self):
        #super().execute()
    
        package_id_str, route_id_str = self.params
        package_id = self._try_parse_int(package_id_str)
        route_id = self._try_parse_int(route_id_str)
        
        package = self.app_data.find_package_by_id(package_id)
        route = self.app_data.find_route_by_id(route_id)

        self.app_data.check_if_package_locations_are_in_route_locations(package, route)
        self.app_data.check_if_package_can_be_adde_to_route(package, route)

        #end_index = route.locations.index(package.end_location)
        #capacity_at_stop = 0
#
        #for i in range(end_index):
        #    capacity_at_stop += route.weight_in_locations[route.locations[i]]
        #
        #if (capacity_at_stop+package.package_weight) > route.truck.capacity:
        #    raise ApplicationError(f'Can\'t assign package #{package_id} to route #{route_id}. Capacity is full!')

        route.update_weight_in_stops(package)
        route.truck.add_package(package)
        
        return f"Package №: {package_id} was added successfuly"
        
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> list[int]:
        return [2]


