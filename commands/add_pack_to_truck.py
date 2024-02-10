from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
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
        route.truck.add_package(package)
        
        return f"Package №: {package_id} was added successfuly"
        
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> list[int]:
        return [2]


