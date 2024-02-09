from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.locations import Locations

class ShowTrucksIn(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        if len(self.params) == 2:
            city = f'{self.params[0]}'+ ' ' + f'{self.params[1]}'
        else:  
            city = self.params[0]

        loc = Locations(city)           

        return f'{loc.show_truck()}'

    def _expected_params_count(self) -> int:
        return 1