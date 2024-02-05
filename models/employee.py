from models.constants.employee_role import EmployeeRole

class Employee():
    def __init__(self, id:int, username:str, first_name:str, last_name:str, password:str, employee_role : EmployeeRole = 'employee') -> None:
        self._id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self._employee_role = employee_role
    
    @property
    def id (self):
        return self._id
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        special_symbols = ['!','£','$','%','&','(',')','<','>','/']
        if len(value) < 2 or len(value) > 20:
            raise  ValueError('Username must be between 2 and 20 characters long!')
        elif [sym for sym in value if sym in special_symbols]:
            raise ValueError('Username contains invalid symbols!')
        else:
            self._username = value
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('Name should be between 3 and 10 symbols.')

        self._first_name = value
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('Name should be between 3 and 10 symbols.')

        self._last_name = value
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        special_symbols = ['!','£','$','%','&','(',')','<','>','/']
        if len(value) < 5 or len(value) > 30:
            raise ValueError('Password must be between 5 and 30 characters long!')
        
        elif [sym for sym in value if sym in special_symbols]:
            raise ValueError('Password contains invalid symbols!')
        
        else:
            self._password = value
    
    @property
    def employee_role(self):
        return self._employee_role
    
    
    