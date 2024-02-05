from models.trucks.trucks import Trucks
from models.package import Package


class ApplicationData:
    def __init__(self) -> None:
        self._all_packages_list: list[Package] = []

    def add_package(self, package: Package):
        if not any(p._package_id == package._package_id for p in self._all_packages_list):
            self._all_packages_list.append(package)
