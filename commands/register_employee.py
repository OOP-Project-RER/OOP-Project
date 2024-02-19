from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.employee_role import EmployeeRole

class RegisterEmployee(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        '''
        RegisterEmployee command creates object of class Employee

        Takes 4 or 5 parameters:
        Case(4) - 1) Username 2)First_name 3) Last_name 4) Password
        Case(5) - 1) Username 2)First_name 3) Last_name 4) Password 5) Employee_role

        Return: String with information
        '''
        #super().execute()
        self._throw_if_employee_logged_in()

        username, firstname, lastname, password, *rest = self.params

        if rest == []:
            employee_role = EmployeeRole.EMPLOYEE
        else:
            employee_role = EmployeeRole.from_string(rest[0])

        employee = self._app_data.create_employee(
            username, firstname, lastname, password, employee_role)
        self._app_data.login(employee)

        return f'User {employee.username} registered successfully!'
    
    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> list[int]:
        return [4, 5]