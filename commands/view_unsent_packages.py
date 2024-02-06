from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.status import Status
from itertools import groupby


class ViewUnsentPackagesCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, searched_location = None):
        super().__init__(params, app_data)
        self._searched_location = searched_location

    @property
    def searched_location(self):
        return self._searched_location

    def execute(self):
        if len(self.params) == 1:
            searched_location = self.params[0]
            unsent_packages = [pack for pack in self.app_data._all_packages_list if pack._status == Status.STENDING and pack._start_location.city == searched_location]
            if unsent_packages:
                sorted_packages = sorted(unsent_packages, key=lambda x: x._start_location.city)
                groups = groupby(sorted_packages, key=lambda x: x._start_location.city)
                result = ""
                for key, group in groups:
                    result += self.format_packages(list(group), key)
                return result
            else:
                return "No unsent packages found."      
            
        elif len(self.params) == 0:
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
            
        else:
             return "Invalid number of parameters. Please provide exactly zero or one location."

    def format_packages(self, packages, location=None):
        total_weight = sum(pack._package_weight for pack in packages)
        amount = len(packages)
        end_locations = [pack._end_location.city for pack in packages]
        if location:
            return f"Start location: {location}\n - Amount of packages: {amount}\n - Total weight: {total_weight}\n - End locations: {end_locations}\n"
        else:
            return f"Total amount of packages: {amount}\nTotal weight: {total_weight}\n"
