from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError
from models.route import Route
from datetime import datetime
from models.constants.locations import Locations

class AddRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory
        

    @property
    def models_factory(self):
        return self._models_factory
    
    def execute(self):
        '''
        AddRouteCommand creates object of class Route 

        Takes from 3 to 10 parameters: 1) Date_Time 2) Location 3) Location 4) Location .......

        Return: String with information for the route
        '''
        #super().execute()

        date_time_departure, *locations = self.params

        date_time_departure = self.app_data.parsed(date_time_departure)
        
        for loc in locations:
            if loc not in Locations.locations:
                raise ApplicationError(f"The city {loc} does not exist")
        
        route: Route = self._models_factory.create_route(date_time_departure, *locations)
        self.app_data.add_route(route)

        return f"Route #{route.route_id} from {locations[0]} created."
    
    def _requires_login(self) -> bool:
         return True

    def _expected_params_count(self) -> list[int]:
        return [3, 10]