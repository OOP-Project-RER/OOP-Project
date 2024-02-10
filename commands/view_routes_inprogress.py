from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.status import Status
from errors.application_error import ApplicationError
from core.models_factory import ModelsFactory
from datetime import datetime


class ViewRoutesCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        #super().execute()
        
        #if self._app_data.logged_in_employee.employee_role != 'Manager':
        #    raise ApplicationError("You are not a manager!")

        routes_in_progres_list = [route.__str__() for route in self._app_data._all_routes_list if route._status == Status.IN_PROGRESS]
        if len(routes_in_progres_list) > 0:
            return '\n'.join(routes_in_progres_list)
        
        return 'There is no routes in progress.'


    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> list[int]:
        return [0]