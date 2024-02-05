from models.employee import Employee
from models.trucks.trucks import Trucks
from models.package import Package


class ApplicationData:
    def __init__(self):
        self._employees = []
        self._logged_employee = None
        self._all_packages_list: list[Package] = []


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

    def add_package(self, package: Package):
        if not any(p._package_id == package._package_id for p in self._all_packages_list):
            self._all_packages_list.append(package)
