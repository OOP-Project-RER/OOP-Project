from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory


class CheckRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        

    def execute(self):
        #super().execute()
        
        start_location, end_lockation = self.params
        route = self.app_data.check_for_route(start_location, end_lockation)
        return "\n".join(route)
    
    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [2]
