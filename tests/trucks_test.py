import unittest
from errors.application_error import ApplicationError
from models.package import Package
from models.route import Route
from datetime import datetime

from models.trucks.trucks import Trucks

VALID_ID = 1001
VALID_NAME = 'Scania'
VALID_CAPACITY = 10000
VALID_MAX_RANGE = 8000
VALID_NUM_OF_TRUCKS = 10


class Initializer_Should(unittest.TestCase):
    def test_assign_values(self):
        # Arrange & Act
        truck = Trucks(VALID_ID, VALID_NAME, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
         # Assert
        self.assertEqual(VALID_ID, truck.truck_id)
        self.assertEqual(VALID_NAME, truck.name)
        self.assertEqual(VALID_CAPACITY, truck.capacity)
        self.assertEqual(VALID_MAX_RANGE, truck.max_range)
        self.assertEqual(VALID_NUM_OF_TRUCKS, truck.num_of_trucks)

class Package_Should(unittest.TestCase):
    def test_pack_returns_tuple(self):
        truck = Trucks(VALID_ID, VALID_NAME, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
        self.assertIsInstance(truck.packages, tuple)

class AddPackage_Should(unittest.TestCase):

    def test_add_package_adds_packages_properly(self):
        #Arrange
        truck = Trucks(VALID_ID, VALID_NAME, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
        package1 = Package(1, "Sydney", "Melbourne", 2000.0, "David Bechkam dave@abv.bg")
        package2 = Package(2, "Sydney", "Adeliade", 1500.0, "David Bechkam dave@abv.bg")
        #Act
        truck.add_package(package1)
        truck.add_package(package2)

        #Assert
        self.assertIn(package1, truck._packages)
        self.assertIn(package2, truck._packages)

class AddRoute_Should(unittest.TestCase):
    def test_add_route_adds_route_properly(self):
        #Arrange
        truck = Trucks(VALID_ID, VALID_NAME, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
    
        route1 = Route(101, datetime.strptime("20240212T0830", "%Y%m%dT%H%M"), "Sydney", "Melbourne")
        route2 = Route(102, datetime.strptime("20240218T0830", "%Y%m%dT%H%M"), "Melbourne", "Adelaide")
        #Act
        truck.add_route(route1)
        truck.add_route(route2)
        #Assert
        self.assertIn(route1, truck._routes_list)
        self.assertIn(route2, truck._routes_list)

class View_Should(unittest.TestCase):
    def test_view_returns_correct_format(self):
        #Arrange
        current_datetime = datetime.now()
        truck = Trucks(VALID_ID, VALID_NAME, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
        package1 = Package(1, "Sydney", "Melbourne", 2000.0, "David Bechkam dave@abv.bg")
        truck.add_package(package1)
        expected = f"#1001. Scania (1 packages)\n  Package: #1\nCreated on: {current_datetime.strftime('%b %d %H:%M')}h\nFrom: Sydney\nTo: Melbourne\nWeight: 2000.0\nStatus: Unassign\nStill in the hub. Its not assign to route, yet!"
        # Act & Assert
        actual = truck.view()
        self.assertEqual(actual, expected)

class Str_Should(unittest.TestCase):
    def test_str_returns_correct_format(self):
        # Arrange
        truck = Trucks(VALID_ID, VALID_NAME, VALID_CAPACITY, VALID_MAX_RANGE, VALID_NUM_OF_TRUCKS)
        package1 = Package(1, "Sydney", "Melbourne", 2000.0, "David Bechkam dave@abv.bg")
        package2 = Package(2, "Sydney", "Adeliade", 1500.0, "David Bechkam dave@abv.bg")
        truck.add_package(package1)
        truck.add_package(package2)
        expected = "#1001. Scania (2 packages)"
        # Act & Assert
        actual = str(truck)
        self.assertEqual(actual, expected)

    