from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.locations import Locations

class ShowTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        #super().execute()
        id_str = self.params[0]  

        id = self._try_parse_int(id_str)

        truck = self.app_data.find_truck_by_id(id)

        #routes_str = []
        #[routes_str.append(route.__str__()) for route in truck._routes_list]

        return '\n'.join([route.__str__() for route in truck._routes_list])

    def _requires_login(self) -> bool:
         return True
    
    def _expected_params_count(self) -> list[int]:
        return [1]