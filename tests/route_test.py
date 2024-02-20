import unittest
from datetime import timedelta, datetime
from errors.application_error import ApplicationError
from models.constants.locations import Locations
from models.constants.status import Status
from models.package import Package
from models.route import Route
from models.trucks.trucks import Trucks

VALID_ID = 101
VALID_DATE_TIME = datetime.strptime("20240212T0830", "%Y%m%dT%H%M")
VALID_LOCATIONS = "Sydney", "Melbourne", "Adelaide"


class Initializer_Should(unittest.TestCase):
    def test_assign_values(self):
        # Arrange & Act
        route = Route(VALID_ID, VALID_DATE_TIME, "Sydney", "Melbourne", "Adelaide")
        # Assert
        self.assertEqual(VALID_ID, route.route_id)
        self.assertEqual(VALID_DATE_TIME, route.date_time_departure)
        self.assertEqual(VALID_LOCATIONS, route.locations)

class Status_Should(unittest.TestCase):
    def test_status_returns_standing(self):
        # Arrange & Act
        route = Route(VALID_ID, VALID_DATE_TIME, "Sydney", "Melbourne", "Adelaide")
        status_datetime = datetime.strptime("20240112T0830", "%Y%m%dT%H%M")
        route.status = status_datetime
        # Assert
        self.assertEqual(route.status, Status.STANDING)

    def test_status_returns_in_progres(self):
        # Arrange & Act
        route = Route(VALID_ID, VALID_DATE_TIME, "Sydney", "Melbourne", "Adelaide")
        status_datetime = datetime.strptime("20240212T0900", "%Y%m%dT%H%M")
        route.status = status_datetime
        # Assert
        self.assertEqual(route.status, Status.IN_PROGRESS)
    
    def test_status_returns_finished(self):
        # Arrange & Act
        route = Route(VALID_ID, VALID_DATE_TIME, "Sydney", "Melbourne", "Adelaide")
        status_datetime = datetime.strptime("20240312T0900", "%Y%m%dT%H%M")
        route.status = status_datetime
        # Assert
        self.assertEqual(route.status, Status.FINISHED)

class AddTruck_Should(unittest.TestCase):
    def test_add_truck_raises_error(self):
        route = Route(VALID_ID, VALID_DATE_TIME, "Sydney", "Melbourne", "Adelaide")
        truck = Trucks(101, "Man", 8000, 200, 1)
        with self.assertRaises(ApplicationError):
            route.add_truck(truck)

class CalculateTravelTime_Should(unittest.TestCase):
    def test_calculate_travel_time(self):
        # Arrange
        route = Route(VALID_ID, VALID_DATE_TIME, "Sydney", "Melbourne", "Adelaide") 
        stop =  "Sydney"
        next_stop = "Melbourne"
        # Act
        expected_travel_time_hours = 877 / 87 
        # Assert
        actual_travel_time_hours = route.calculate_travel_time(stop, next_stop)
        self.assertEqual(actual_travel_time_hours, expected_travel_time_hours)

class StopInfo_Should(unittest.TestCase):
    def test_stops_info_returns_correct_output(self):
        # Arrange
        route = Route(VALID_ID, VALID_DATE_TIME, "Sydney", "Melbourne", "Adelaide")
        # Act
        expected_stops_date_time = {
            Locations.SYD: datetime.strptime("20240212T0830", "%Y%m%dT%H%M"), 
            Locations.MEL: datetime(2024, 2, 12, 18, 34, 49, 655172),
            Locations.ADL: datetime(2024, 2, 13, 2, 54, 49, 655172)  
        }
        expected_weight_in_locations = {
            Locations.SYD: 0,  
            Locations.MEL: 0,  
            Locations.ADL: 0   
        }
        stops_date_time, weight_in_locations = route.stops_info()
        # Assert
        self.assertEqual(stops_date_time, expected_stops_date_time)
        self.assertEqual(weight_in_locations, expected_weight_in_locations)

class GenerateRouteString_Should(unittest.TestCase):
    def test_generate_route_string_returns_string_properly(self):
        # Arrange & Act
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        expected_output = "Sydney (Feb 10 02:55h) → Melbourne (Feb 10 12:59h) → Adelaide (Feb 10 21:19h)"
        # Assert
        self.assertEqual(route.generate_route_string(), expected_output)

class CalculateCurrentLocations_Should(unittest.TestCase):
    def test_calc_current_locations_when_in_local_hub(self):
        # Arrange & Act
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        now = datetime.strptime("20240208T0255", "%Y%m%dT%H%M")
        expected_output = "Still in local hub: Sydney"
        # Assert
        self.assertEqual(route.calc_current_locations(now), expected_output)

    def test_calc_current_locations_when_in_progress(self):
        # Arrange & Act
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        now = datetime.strptime("20240210T0455", "%Y%m%dT%H%M")
        expected_output = "703 km till Melbourne"
        # Assert
        self.assertEqual(route.calc_current_locations(now), expected_output)
        

    def test_calc_current_locations_when_finished(self):
        # Arrange & Act
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        expected_output = "Reached end location: Adelaide"
        # Assert
        self.assertEqual(route.calc_current_locations(), expected_output)

class UpdateWeightInStops_Should(unittest.TestCase):
    def test_update_weight_in_stops(self):
        # Arrange
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        package = Package(1, "Sydney", "Melbourne", 2000.0, "David Bechkam dave@abv.bg")
        # Act
        route.update_weight_in_stops(package)
        expected_weight_in_locations = {
        Locations.SYD: 2000,  
        Locations.MEL: -2000, 
        Locations.ADL: 0  
        }
        # Assert
        self.assertEqual(route.weight_in_locations, expected_weight_in_locations)

class RemovePackage_Should(unittest.TestCase):
    def test_remove_package(self):
        # Arrange
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        package = Package(1, "Sydney", "Melbourne", 2000.0, "David Bechkam dave@abv.bg")
        # Act
        route.remove_package(package)
        expected_weight_in_locations = {
        Locations.SYD: -2000.0,  
        Locations.MEL: 2000.0, 
        Locations.ADL: 0
        }
        # Assert
        self.assertEqual(route.weight_in_locations, expected_weight_in_locations)

class TotalDistance_Sould(unittest.TestCase):
    def test_total_distance(self):
        # Arrange & Act
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        expected_output = 1602
        # Assert
        self.assertEqual(route.calc_total_distance(), expected_output)

class Str_Should(unittest.TestCase):
    def test_str_returns_correct_format(self):
        # Arrange & Act
        route = Route(VALID_ID, datetime.strptime("20240210T0255", "%Y%m%dT%H%M"), "Sydney", "Melbourne", "Adelaide")
        expected_output = f'''Route #101
{route.locations[0]} (Feb 10 02:55h) → {route.locations[1]} (Feb 10 12:59h) → {route.locations[2]} (Feb 10 21:19h)
Total distance: 1602
Current locations: Reached end location: {route.locations[2]}'''
        actual = str(route)
        # Assert
        self.assertEqual(actual, expected_output)
