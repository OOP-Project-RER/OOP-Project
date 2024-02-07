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
        # super().execute(params)

        # if not self._app_data.logged_in_employee.employee_role.MANAGER:
        #     raise ApplicationError("You are not a manager!")

        pass

    # def _requires_login(self) -> bool:
    #     return True

    def _expected_params_count(self) -> int:
        return 0