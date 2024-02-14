from models.constants.employee_role import EmployeeRole
from errors.application_error import ApplicationError

class Employee():
    def __init__(self, username:str, first_name:str, last_name:str, password:str, employee_role : EmployeeRole = 'Employee') -> None:
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self._employee_role = EmployeeRole.from_string(employee_role)

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        special_symbols = ['!','£','$','%','&','(',')','<','>','/']
        if len(value) < 2 or len(value) > 20:
            raise  ApplicationError('Username must be between 2 and 20 characters long!')
        elif [sym for sym in value if sym in special_symbols]:
            raise ApplicationError('Username contains invalid symbols!')
        else:
            self._username = value
    
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter 
    def first_name(self, value):
        if type(value) != str:
            raise ApplicationError('Name should be letters')
        elif len(value) < 2 or len(value) > 15:
            raise ApplicationError('Name should be between 3 and 10 symbols.')
        else:
            self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter 
    def last_name(self, value):
        if type(value) != str:
            raise ApplicationError('Name should be letters')
        elif len(value) < 2 or len(value) > 15:
            raise ApplicationError('Name should be between 3 and 10 symbols.')
        else:
            self._last_name = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        special_symbols = ['!','£','$','%','&','(',')','<','>','/']
        if len(value) < 5 or len(value) > 30:
            raise ApplicationError('Password must be between 5 and 30 characters long!')
        
        elif [sym for sym in value if sym in special_symbols]:
            raise ApplicationError('Password contains invalid symbols!')
        
        else:
            self._password = value
    
    @property
    def employee_role(self):
        return self._employee_role
    
    
    