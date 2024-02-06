from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count
from models.constants.locations import Locations
from models.constants.status import PackageStatus
from itertools import groupby


class ViewUnsentPackagesCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, surched_location = None):
        super().__init__(params, app_data)
        self._surched_location = surched_location
        validate_params_count(params, 1)

    @property
    def surched_location(self):
        return self._surched_location

    def execute(self):

        if self._surched_location != None:
            sorted_packages = sorted([pack for pack in self.app_data._all_packages_list if pack._status == PackageStatus.STENDING], key=lambda x: x._start_location)
            groups = groupby(sorted_packages, key=lambda x: x._start_location)

            for key, group in groups:
                group_list = list(group)
                total_waight = sum([w[3] for w in group_list])
                amount = len(group_list)
                end_locations = [l[1] for l in group_list]
                if key == self._surched_location:
                    result = f'''Start location: {key}
                    - Amount of packages: {amount}
                    - Total waight: {total_waight}
                    - End locations: {list(end_locations)}'''
                    return result
                else:
                    result = f'''Start location: {key}
                    - Amount of packages: {amount}
                    - Total waight: {total_waight}
                    - End locations: {list(end_locations)}'''
                    return result