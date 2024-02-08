from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory

class AssignTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory : ModelsFactory):
        self._models_factory = models_factory
        super().__init__(params, app_data)

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        #return super().execute()
        vehicle = self.params[0]
        id = self._try_parse_int(self.params[1])
        route = self._app_data.find_route_by_id(id)

        truck = self.models_factory.create_truck(vehicle)
        route.add_truck(truck)

        return f'{vehicle} truck was assigh to route #{self.params[1]}'



        