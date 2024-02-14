from errors.application_error import ApplicationError

class Customer:
    def __init__(self,first_name:str, last_name:str, email:str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    def check_first_name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ApplicationError('Firstname must be between 2 and 20 characters long!')
    
        return value
    
    def check_last_name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ApplicationError('Firstname must be between 2 and 20 characters long!')
    
        return value
    
    def check_email(self, value):
        if '@' not in value:
            raise ApplicationError('You enter a invalid email!(Should contain "@")')
        
        return value