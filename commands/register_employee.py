from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.employee_role import EmployeeRole




class RegisterEmployee(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        #super().execute()
        username, firstname, lastname, password, *rest = self.params

        if rest == []:
            employee_role = EmployeeRole.EMPLOYEE
        else:
            employee_role = EmployeeRole.from_string(rest[0])

        user = self._app_data.create_user(
            username, firstname, lastname, password, employee_role)
        #self._app_data.login(user)

        return f'User {user.username} registered successfully!'
