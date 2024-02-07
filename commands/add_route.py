from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from models.route import Route

class AddRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory
        

    @property
    def models_factory(self):
        return self._models_factory
    
    def execute(self):
        start_location, *other_locations = self.params
        route: Route = self._models_factory.create_route(self, start_location, *other_locations)
        self.app_data.add_route(route)

        return f"Route #{route.route_id} from {start_location} created."