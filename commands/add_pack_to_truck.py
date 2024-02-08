from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.trucks.trucks import Trucks


class AddPackToTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)


    def execute(self):
        package_id_str, = self.params
        package_id = self._try_parse_int(package_id_str)
        package = self.app_data.find_package_by_id(package_id)
        Trucks.add_package(package)   #тук гърми :(
        return f"Package №: {package_id} was added to truck №: {Trucks.truck_id}"
        


