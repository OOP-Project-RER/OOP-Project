from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start() 


# addroute 20240210T1630 Sydney Melbourne
# assigntruck Man 101
# addpackage Sydney Melbourne 2350 gosho gosho gosho@abv.bg
# addpacktotruck 1 101