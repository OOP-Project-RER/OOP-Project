from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory


class CheckRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        

    def execute(self):
        
        start_location, end_lockation = self.params
        route = self.app_data.check_for_route(start_location, end_lockation)
        return ",  ".join(route)
