from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import  try_parse_int

class FindPackage(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        p_id = try_parse_int(self.params[0])

        package = self.app_data.find_package_by_id(p_id)

        return (f'{package}\n\nEmail with this information was send to {package.contact_customer.email}')
                