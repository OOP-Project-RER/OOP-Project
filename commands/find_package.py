from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from datetime import datetime

class FindPackageCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        #super().execute()

        p_id = self._try_parse_int(self.params[0])

        package = self.app_data.find_package_by_id(p_id)
        package.status = datetime.now()

        return (f'{package}\n\nEmail with this information was send to {package.contact_customer.email}')
    
    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [1]