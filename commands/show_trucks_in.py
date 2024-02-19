from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.locations import Locations

class ShowTrucksIn(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        '''
        ShowTrucksIn command is showing in every city how many trucks have at the moment

        Takes 1 parameter: 1) Location

        Return: String with information for the number of trucks in location
        '''
        #super().execute()

        loc = Locations.from_string(self.params[0])          

        return f'{Locations.show_truck(loc)}'
    def _requires_login(self) -> bool:
         return True
    
    def _expected_params_count(self) -> list[int]:
        return [1]