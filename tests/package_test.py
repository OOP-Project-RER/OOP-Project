from datetime import datetime, timedelta
import unittest
from errors.application_error import ApplicationError
from models.constants.status import Status
from models.package import Package

VALID_ID = 3
VALID_START_LOCATION = "Sydney"
VALID_END_LOCATION = "Adelaide"
VALID_WEIGHT = 1500
VALID_CUSTOMER_CONTACT = "David Bechkam dave@abv.bg"
VALID_DEPARTURE_TIME= datetime.now() + timedelta(hours=1)
VALID_ARIVAL_TIME = datetime.now() + timedelta(hours=8)

class Package_Should(unittest.TestCase):
    def test_init_assign_values_properly(self):
        # Arrange & Act
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        # Assert
        self.assertEqual(VALID_ID, package.package_id)
        self.assertEqual(VALID_START_LOCATION, package.start_location)
        self.assertEqual(VALID_END_LOCATION, package.end_location)
        self.assertEqual(VALID_WEIGHT, package.package_weight)
        self.assertEqual(VALID_CUSTOMER_CONTACT, package.contact_customer)

    def test_error_is_raised_when_weight_less_than_zero(self):
        with self.assertRaises(ApplicationError):
           package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, -2, VALID_CUSTOMER_CONTACT) 

    def test_status_returns_unassign(self):
        # Arrange & Act
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        package._departure_time = None
        package.status = datetime.now()
        # Assert
        self.assertEqual(package.status, Status.UNASSIGN)

    def test_status_returns_standing(self):
        # Arrange & Act
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        package._departure_time = VALID_DEPARTURE_TIME
        package.status = datetime.now()
        # Assert
        self.assertEqual(package.status, Status.STANDING)

    def test_status_returns_in_progress(self):
        # Arrange & Act
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        package._departure_time = VALID_DEPARTURE_TIME
        package._arriving_time = VALID_ARIVAL_TIME
        now = package._departure_time + timedelta(minutes=90)
        package.status = now
        # Assert
        self.assertEqual(package.status, Status.IN_PROGRESS)
    
    def test_status_returns_finished(self):
        # Arrange & Act
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        package._departure_time = VALID_DEPARTURE_TIME
        package._arriving_time = VALID_ARIVAL_TIME
        now = package._arriving_time + timedelta(minutes=90)
        package.status = now
        # Assert
        self.assertEqual(package.status, Status.FINISHED)

    def test_current_location_before_departure(self):
        # Arrange & Act
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        package._departure_time = VALID_DEPARTURE_TIME
        now =  package._departure_time - timedelta(minutes=30)
        expected_result = f'Still in {VALID_START_LOCATION} hub. Waiting for the truck!'
        # Assert
        self.assertEqual(package.current_location(), expected_result)

    def test_current_location_after_arrival(self):
        # Arrange & Act
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        package._departure_time = VALID_DEPARTURE_TIME
        package._arriving_time = VALID_ARIVAL_TIME
        now = package._arriving_time + timedelta(minutes=90)
        expected_result = f'Reached end location: {VALID_END_LOCATION}'
        # Assert
        self.assertEqual(package.current_location(), expected_result)

    def test_str_returns_correct_format(self):
        # Arrange
        current_datetime = datetime.now()
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CUSTOMER_CONTACT)
        expected = f'''Package: #{VALID_ID}
Created on: {current_datetime.strftime('%b %d %H:%M')}h
From: {VALID_START_LOCATION}
To: {VALID_END_LOCATION}
Weight: {VALID_WEIGHT}
Status: {Status.UNASSIGN}
Still in the hub. Its not assign to route, yet!'''
        # Act & Assert
        actual = str(package)
        self.assertEqual(actual, expected)
        