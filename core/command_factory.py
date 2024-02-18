from errors.application_error import ApplicationError
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.register_employee import RegisterEmployee
from commands.logout_command import LogoutCommand
from commands.login_command import LoginCommand
from commands.add_package import AddPackageCommand
from commands.show_trucks_in import ShowTrucksIn
from commands.view_unsent_packages import ViewUnsentPackagesCommand
from commands.add_route import AddRouteCommand
from commands.find_package import FindPackageCommand
from commands.view_routes_inprogress import ViewRoutesCommand
from commands.check_route import CheckRouteCommand
from commands.assign_truck import AssignTruck
from commands.add_pack_to_route import AddPackToRoute
from commands.remove_package import RemovePackage
from commands.show_truck import ShowTruck

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == 'registeremployee':
            return RegisterEmployee(params, self._app_data)
        if cmd.lower() == 'logout':
            return LogoutCommand(params, self._app_data)
        if cmd.lower() == 'login':
            return LoginCommand(params, self._app_data)
        if cmd.lower() == 'addpackage':
            return AddPackageCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == 'showtrucksin':
            return ShowTrucksIn(params, self._app_data)
        if cmd.lower() == 'viewunsentpackages': 
            return ViewUnsentPackagesCommand(params, self._app_data)
        if cmd.lower() == 'addroute':
            return AddRouteCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == 'findpackage':
            return FindPackageCommand(params, self._app_data)
        if cmd.lower() == 'viewroutes':
            return ViewRoutesCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == 'checkroute':
            return CheckRouteCommand(params, self._app_data)
        if cmd.lower() == 'assigntruck':
            return AssignTruck(params, self._app_data, self._models_factory)
        if cmd.lower() == 'addpacktoroute':
            return AddPackToRoute(params, self._app_data)
        if cmd.lower() == 'removepackfromroute':
            return RemovePackage(params, self._app_data)
        if cmd.lower() == 'showtruck':
            return ShowTruck(params, self._app_data)
        
        
        
        raise ApplicationError(f'Invalid command name: {cmd}!')