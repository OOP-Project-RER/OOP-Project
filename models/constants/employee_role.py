from errors.application_error import ApplicationError


class EmployeeRole:
    EMPLOYEE = 'Employee'
    SUPERVISOR = 'Supervisor'
    MANAGER = 'Manager'

    @classmethod
    def from_string(cls, value) -> str:
        '''Method which check if value match the class attributes'''
        if value not in [cls.EMPLOYEE, cls.SUPERVISOR, cls.MANAGER]:
            raise ApplicationError(
                f'None of the possible EmployeeRole values matches the value {value}.')

        return value

