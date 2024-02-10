from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from models.customer import Customer
from models.constants.locations import Locations
from errors.application_error import ApplicationError

class AddPackageCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        
        self._models_factory = models_factory
        super().__init__(params, app_data)

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        #super().execute()

        start_location_str, end_location_str, package_weight_str, *contact_customer_str = self.params
        package_weight = self._try_parse_float(package_weight_str)
        start_location = Locations(start_location_str)
        end_location = Locations(end_location_str)
        contact_customer = Customer(*contact_customer_str)
        package = self.models_factory.create_package(start_location, end_location, package_weight, contact_customer)
        self.app_data.add_package(package)

        return f'Package #{package.package_id} with weight {package_weight} was added to the waiting list.'
    
    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [6]