from models.employee import Employee

class ApplicationData:
    def __init__(self):
        self._employees = []
        self._logged_employee = None

    @property
    def employees(self):
        return tuple(self._employees)

    def create_user(self, username, firstname, lastname, password, user_role) -> Employee:
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ValueError(
                f'User {username} already exist. Choose a different username!')

        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)

        return employee