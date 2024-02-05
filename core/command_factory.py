from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.register_employee import RegisterEmployee

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "registeremployee":
            return RegisterEmployee(params, self._app_data)