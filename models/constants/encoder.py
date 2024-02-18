from json import JSONEncoder
# from core.application_data import ApplicationData
from models.package import Package
from models.trucks.trucks import Trucks
from models.route import Route
from models.customer import Customer
from models.employee import Employee
from datetime import datetime

class Encoder(JSONEncoder):
    def default(self, o):
        
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        
        elif isinstance(o, Package):
            return o.__dict__
        
        elif isinstance(o, Trucks):
            return o.__dict__

        elif isinstance(o, Route):
            return o.__dict__
        
        elif isinstance(o, Customer):
            return o.__dict__
        
        elif isinstance(o, Employee):
            return o.__dict__
        else:
            return super().default(o)
