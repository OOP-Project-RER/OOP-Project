from comands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from comands.validation_helpers import validate_params_count, try_parse_float, try_parse_int
from models.customer import Customer

class AddPackageCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        super().__init__(params, app_data)
        validate_params_count(params, 5)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        package_id_str, start_location, end_location, package_weight_str, contact_customer_str = self._params
        package_id = try_parse_int(package_id_str)
        package_weight = try_parse_float(package_weight_str)
        contact_customer = Customer(contact_customer_str)
        package = self.models_factory.create_package(package_id, start_location, end_location, package_weight, contact_customer)
        self.app_data.add_package(package)

        return f'Package #{package_id} was added to the waiting list.'
