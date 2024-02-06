from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count
from models.constants.status import Status
from itertools import groupby


class ViewUnsentPackagesCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, searched_location = None):
        super().__init__(params, app_data)
        self._searched_location = searched_location
        validate_params_count(params, 1)

    @property
    def searched_location(self):
        return self._searched_location

    def execute(self):
        if self._searched_location:
            unsent_packages = [pack for pack in self.app_data._all_packages_list if pack._status == Status.STENDING and pack._start_location == self._searched_location]
            if unsent_packages:
                return self.format_packages(unsent_packages)
            else:
                return f"No unsent packages found for the location '{self._searched_location}'."
        else:
            unsent_packages = [pack for pack in self.app_data._all_packages_list if pack._status == Status.STENDING]
            if unsent_packages:
                sorted_packages = sorted(unsent_packages, key=lambda x: x._start_location.city)
                groups = groupby(sorted_packages, key=lambda x: x._start_location.city)
                result = ""
                for key, group in groups:
                    result += self.format_packages(list(group), key)
                return result
            else:
                return "No unsent packages found."

    def format_packages(self, packages, location=None):
        total_weight = sum(pack._package_weight for pack in packages)
        amount = len(packages)
        end_locations = [pack._end_location.city for pack in packages]
        if location:
            return f"Start location: {location}\n - Amount of packages: {amount}\n - Total weight: {total_weight}\n - End locations: {end_locations}\n"
        else:
            return f"Total amount of packages: {amount}\nTotal weight: {total_weight}\n"
