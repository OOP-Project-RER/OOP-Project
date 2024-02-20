from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData



class LogoutCommand(BaseCommand):
    def __init__(self,params, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        '''
        LogoutCommand is logging out the user who is logged in

        Takes no parameter

        Return string with information
        '''
        super().execute()
        
        self._app_data.logout()

        return 'You logged out!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> list[int]:
        return [0]
