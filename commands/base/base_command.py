from core.application_data import ApplicationData
from errors.application_error import ApplicationError


class BaseCommand():
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    @property
    def params(self):
        return tuple(self._params)

    @property
    def app_data(self):
        return self._app_data

    def execute(self):
        if self._requires_login() and not self._app_data.has_logged_in_employee:
            raise ApplicationError('You are not logged in! Please login first!')
        
        if len(self._expected_params_count()) == 2:
            if len(self.params) < self._expected_params_count()[0] or len(self.params) > self._expected_params_count()[1]:
                raise ApplicationError(
                    f'Invalid number of arguments. Expected between {self._expected_params_count()[0]} and {self._expected_params_count()[1]} arguments, Received: {len(self.params)}')
        else:
            if len(self.params) != self._expected_params_count()[0]:
                raise ApplicationError(
                    f'Invalid number of arguments. Expected {self._expected_params_count()[0]}')
        return ''
    
    
    def _try_parse_float(self, s, msg='Invalid value. Expected a float.'):
        try:
            return float(s)
        except:
            raise ApplicationError(msg)
        

    def _try_parse_int(self, s, msg='Invalid value. Expected an int.'):
        try:
            return int(s)
        except:
            raise ApplicationError(msg)

    
    def _requires_login(self) -> bool:
        raise NotImplementedError('Override in derived class')

    def _expected_params_count(self) -> list[int]:
        raise NotImplementedError('Override in derived class')
    
    def _throw_if_employee_logged_in(self):
        if self._app_data.has_logged_in_employee:
            logged_employee = self._app_data.logged_in_employee
            raise ApplicationError(
                f'Employee {logged_employee.username} is logged in! Please log out first!')
