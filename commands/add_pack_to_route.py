from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from errors.application_error import ApplicationError
from models.trucks.trucks import Trucks
from models.constants.status import Status


class AddPackToRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)


    def execute(self):
        #super().execute()
    
        package_id_str, route_id_str = self.params
        package_id = self._try_parse_int(package_id_str)
        route_id = self._try_parse_int(route_id_str)
        
        package = self.app_data.find_package_by_id(package_id)
        route = self.app_data.find_route_by_id(route_id)

        if package.status != Status.UNASSIGN:
            raise ApplicationError('This package was already assign to route!')

        self.app_data.check_if_package_is_already_added(package, route)
        self.app_data.check_if_package_locations_are_in_route_locations(package, route)
        self.app_data.check_if_package_weight_can_be_adde_to_route(package, route)

        route.truck.add_package(package)
        route.update_weight_in_stops(package)

        package._departure_time = route._stops_date_time[package.start_location]
        package._arriving_time = route._stops_date_time[package.end_location]
        
        return f"Package №: {package_id} was added successfuly"
        
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> list[int]:
        return [2]


