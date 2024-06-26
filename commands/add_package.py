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
        '''
        AddPackageCommand creates object of class Package and object of class Customer

        Takes 6 parameters: 1) Start_Location 2) End_Location 3) Package weight 4) Customer name 5) Customer surname 6) Customer email

        Return: String with information for the package
        '''
        #super().execute() 

        start_location_str, end_location_str, package_weight_str, *contact_customer_str = self.params
        package_weight = self._try_parse_float(package_weight_str)
        start_location = Locations.from_string(start_location_str) 
        end_location = Locations.from_string(end_location_str)  
        contact_customer = Customer(*contact_customer_str)
        package = self.models_factory.create_package(start_location, end_location, package_weight, contact_customer)
        self.app_data.add_package(package)

        return f'Package #{package.package_id} with weight {package_weight} was added to the waiting list.'
    
    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [6]