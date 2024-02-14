import unittest
from errors.application_error import ApplicationError
from models.constants.employee_role import EmployeeRole
from models.employee import Employee

VALID_USERNAME = "pesho_123"
VALID_FIRST_NAME = "Petar"
VALID_LAST_NAME = "Petrov"
VALID_PASSWORD = "Password.123"
VALID_EMPLOYEE_ROLE = EmployeeRole.EMPLOYEE

class Initializer_Should(unittest.TestCase):
    def test_assign_values(self):
        # Arrange & Act
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_EMPLOYEE_ROLE)
        #Assert
        self.assertEqual(VALID_USERNAME, employee.username)
        self.assertEqual(VALID_FIRST_NAME, employee.first_name)
        self.assertEqual(VALID_LAST_NAME, employee.last_name)
        self.assertEqual(VALID_PASSWORD, employee.password)
        self.assertEqual(VALID_EMPLOYEE_ROLE, employee.employee_role)
    
    def test_raise_error_invalid_username(self):
        with self.assertRaises(ApplicationError):
            Employee("_", VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_EMPLOYEE_ROLE)

    def test_raise_error_invalid_symbols_used_in_username(self):
        with self.assertRaises(ApplicationError):
            Employee("gosho!%", VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_EMPLOYEE_ROLE)

    def test_raise_error_invalid_first_name(self):
        with self.assertRaises(ApplicationError):
            Employee(VALID_USERNAME, "_", VALID_LAST_NAME, VALID_PASSWORD, VALID_EMPLOYEE_ROLE)
    
    def test_raise_error_when_first_name_not_letters(self):
        with self.assertRaises(ApplicationError):
            Employee(VALID_USERNAME, 12345, VALID_LAST_NAME, VALID_PASSWORD, VALID_EMPLOYEE_ROLE)

    def test_raise_error_invalid_last_name(self):
        with self.assertRaises(ApplicationError):
            Employee(VALID_USERNAME, VALID_FIRST_NAME, "_", VALID_PASSWORD, VALID_EMPLOYEE_ROLE)

    def test_raise_error_when_last_name_not_letters(self):
        with self.assertRaises(ApplicationError):
            Employee(VALID_USERNAME, VALID_FIRST_NAME, 12345, VALID_PASSWORD, VALID_EMPLOYEE_ROLE)
    
    def test_raise_error_invalid_password(self):
        with self.assertRaises(ApplicationError):
            Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, "_", VALID_EMPLOYEE_ROLE)  

    def test_raise_error_when_password_contains_invalid_symbols(self):
        with self.assertRaises(ApplicationError):
            Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, "password!!", VALID_EMPLOYEE_ROLE)