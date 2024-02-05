from errors.application_error import ApplicationError
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output: list[str] = []
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                command = self._command_factory.create(input_line)
                #output.append(command.execute())
                print('-----------------------')
                print(command.execute())
                print()
            except ApplicationError as e:
                print(e)
            except Exception as err:
                #output.append(err.args[0])
                print(err.args[0])
                print()

        print('\n'.join(output))
