from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.application_data import ApplicationError
from models.constants.status import Status
from datetime import datetime

class RemovePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        '''
        RemovePackage command is removing assigned package from route

        Takes 2 parameters: 1) Pakage_id 2) Route_id

        Return: String with information for the state of the package
        '''
    #super().execute()
        package_id_str, route_id_str = self.params
        package_id = self._try_parse_int(package_id_str)
        route_id = self._try_parse_int(route_id_str)

        route = self.app_data.find_route_by_id(route_id)
        package = self.app_data.find_package_by_id(package_id)
        package.status = datetime.now()
        if package.status == Status.IN_PROGRESS:
            raise ApplicationError(f'Package #{package.package_id} is In progress and can\'t remove it!')
        
        try:
            route.truck.remove_package(package)
            route.remove_package(package)
        except:
            raise ApplicationError(f'Package #{package_id} is not on this route!')
       
        return f'Package #{package_id} with weight {package.package_weight} was removed from route #{route_id}'
    
    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [2]
        
        