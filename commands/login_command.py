from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from errors.application_error import ApplicationError


class LoginCommand(BaseCommand):
    def __init__(self,params, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        #super().execute()
        self._throw_if_employee_logged_in()

        username, password = self.params
        employee = self._app_data.find_employee_by_username(username)
        if employee.password != password:
            raise ApplicationError('Wrong username or password!')
        else:
            self._app_data.login(employee)

            return f'User {employee.username} successfully logged in!'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> list[int]:
        return [2]
