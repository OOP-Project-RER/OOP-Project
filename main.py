from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start() 

# registeremployee dave David Bechkam 12345
# addroute 20240212T0830 Sydney Melbourne Adelaide
# assigntruck Man 101
# addpackage Sydney Melbourne 2350 gosho gosho gosho@abv.bg
# addpacktotruck 1 101
# viewunsentpackages
# showtrucksin Adelaide
# viewroutes
# checkroute Melbourne Adelaide
# findpackage 


# addroute 20240212T0830 Sydney Melbourne Adelaide Brisbane
# assigntruck Man 101
# addpackage Sydney Brisbane 20000 gosho gosho gosho@abv.bg
# addpackage Adelaide Brisbane 4000 gosho gosho gosho@abv.bg
# addpackage Melbourne Brisbane 3350 gosho gosho gosho@abv.bg
# addpackage Melbourne Brisbane 10050 gosho gosho gosho@abv.bg
# addpacktotruck 1 101
# addpacktotruck 2 101
# addpacktotruck 3 101

# addroute 20240212T0830 Sydney Melbourne Adelaide
# addroute 20240214T1800 Sydney Melbourne Adelaide
# addroute 20240215T0830 Sydney Melbourne Adelaide
# addroute 20240215T1000 Sydney Melbourne Adelaide
# addroute 20240215T1000 Sydney Melbourne Adelaide
# assigntruck Man 101
# assigntruck Man 102

