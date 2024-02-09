from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
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
        valid_locations = []
        date_time_departure, *locations_str = self.params
        for loc in locations_str:
            if loc not in Locations.locations:
                raise ValueError(f"The city {loc} does not exist")
        for location in Locations.locations:
            for loc in locations_str:
                if location == loc:
                    valid_locations.append(loc)
        route: Route = self._models_factory.create_route(date_time_departure, *valid_locations)
        self.app_data.add_route(route)

        return f"Route #{route.route_id} from {valid_locations[0]} created."