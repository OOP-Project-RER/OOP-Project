from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from models.constants.locations import Locations

class CheckRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)       

    def execute(self):
        '''
        CheckRouteCommand is checking for routes between 2 locations 

        Takes 2 locations as parameters: 1) Start_location 2) End_location

        Return: String with information for every route between the 2 locations
        '''
        #super().execute()
        
        start_location_str, end_lockation_str = self.params

        start_location = Locations.from_string(start_location_str)
        end_location = Locations.from_string(end_lockation_str)

        route = self.app_data.check_for_route(start_location, end_location)
        return "\n".join(route)
    
    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [2]
