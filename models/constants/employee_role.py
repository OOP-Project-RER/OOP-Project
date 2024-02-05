class EmployeeRole:
    EMPLOYEE = 'employee'
    SUPERVISOR = 'supervisor'
    MANAGER = 'manager'

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.EMPLOYEE, cls.SUPERVISOR, cls.MANAGER]:
            raise ValueError(
                f'None of the possible EmployeeRole values matches the value {value}.')

        return value

