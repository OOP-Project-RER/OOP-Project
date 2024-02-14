import unittest
from errors.application_error import ApplicationError
from models.customer import Customer

VALID_FIRST_NAME = "Petar"
VALID_LAST_NAME = "Petrov"
VALID_EMAIL = "pesho@abv.bg"

class Initializer_Should(unittest.TestCase):
    def test_assign_values(self):
        # Arrange & Act
        customer = Customer(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL)
        # Assert
        self.assertEqual(VALID_FIRST_NAME, customer.first_name)
        self.assertEqual(VALID_LAST_NAME, customer.last_name)
        self.assertEqual(VALID_EMAIL, customer.email)

class CheckFirstName_Sould(unittest.TestCase):
    def test_raise_error_invalid_first_name(self):
        # Arrange
        customer = Customer(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL)    
        # Act & Assert
        with self.assertRaises(ApplicationError) as context:
            customer.check_first_name("_")
            self.assertEqual(str(context.exception))

class CheckLastName_Should(unittest.TestCase):
    def test_raise_error_invalid_last_name(self):
        # Arrange
        customer = Customer(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL)    
        # Act & Assert
        with self.assertRaises(ApplicationError) as context:
            customer.check_last_name("_")
            self.assertEqual(str(context.exception))

class CheckEmail_Should(unittest.TestCase):
    def test_raise_error_invalid_email(self):
        # Arrange
        customer = Customer(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL)
        # Act & Assert
        with self.assertRaises(ApplicationError) as context:
            customer.check_email("gosho.abv.bg")
            self.assertEqual(str(context.exception))
    