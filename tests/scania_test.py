import unittest
from errors.application_error import ApplicationError
from models.constants.name import Name
from models.trucks.scania import Scania

VALID_ID = 1001
VALID_NAME = Name.SCANIA
VALID_CAPACITY = 42000
VALID_MAX_RANGE = 8000
VALID_NUM_OF_TRUCKS = 10


class Scania_Should(unittest.TestCase):
    def test_assign_values(self):
        # Arrange & Act
        truck = Scania(VALID_NAME,VALID_ID, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
         # Assert
        self.assertEqual(VALID_ID, truck.truck_id)
        self.assertEqual(VALID_NAME, truck.name)
        self.assertEqual(VALID_CAPACITY, truck.capacity)
        self.assertEqual(VALID_MAX_RANGE, truck.max_range)
        self.assertEqual(VALID_NUM_OF_TRUCKS, truck.num_of_trucks)
    
    def test_truckID_increases_when_assigned(self):
        # Arrange & Act
        truck1 = Scania(VALID_NAME,VALID_ID, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
        truck2 = Scania(VALID_NAME,VALID_ID, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
        man1_id = truck1.truck_id
        man2_id = truck2.truck_id
        # Assert
        self.assertGreater(man2_id, man1_id)

    def test_truckID_raises_error_when_ID_greater(self):
        # Arrange & Act
        truck = Scania(VALID_NAME, 1011, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
        # Assert
        with self.assertRaises(ApplicationError):
            truck.truck_id = 1011

        

