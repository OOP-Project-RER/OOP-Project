import unittest
from commands.add_pack_to_route import AddPackToRoute
from commands.add_package import AddPackageCommand
from commands.assign_truck import AssignTruck
from commands.check_route import CheckRouteCommand
from commands.find_package import FindPackageCommand
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.register_employee import RegisterEmployee
from commands.show_trucks_in import ShowTrucksIn
from commands.view_routes_inprogress import ViewRoutesCommand
from commands.view_unsent_packages import ViewUnsentPackagesCommand
from commands.add_route import AddRouteCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError


class Create_Should(unittest.TestCase):
    def test_raise_error_invalid_command_name(self):
        # Arrange
        input_line = "asd 1 2 3"
        cmd_factory = CommandFactory(ApplicationData)
       
        # Act & Assert
        with self.assertRaises(ApplicationError):
            command = cmd_factory.create(input_line)

    def test_create_register_employee_command(self):
        # Arrange
        input_line = "registeremployee dave David Bechkam 12345"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, RegisterEmployee)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(("dave", "David", "Bechkam", "12345"), command.params)

    def test_create_logout_command(self):
        # Arrange
        input_line = "logout"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, LogoutCommand)
        self.assertEqual(app_data, command.app_data)
        
    def test_create_login_command(self):
        # Arrange
        input_line = "login dave 12345"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, LoginCommand)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(("dave", "12345"), command.params)

    def test_create_add_package_command(self):
        # Arrange
        input_line = "addpackage Sydney Melbourne 2350 David Bechkam dave@abv.bg"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, AddPackageCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(("Sydney", "Melbourne", "2350", "David", "Bechkam", "dave@abv.bg"), command.params)

    def test_create_show_trucks_in_command(self):
        # Arrange
        input_line = "showtrucksin"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, ShowTrucksIn)
        self.assertEqual(app_data, command.app_data)
        
    def test_create_view_unsent_packages_command(self):
        # Arrange
        input_line = "viewunsentpackages"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, ViewUnsentPackagesCommand)
        self.assertEqual(app_data, command.app_data)

    def test_create_add_route_command(self):
        # Arrange
        input_line = "addroute 20240212T0830 Sydney Melbourne Adelaide"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, AddRouteCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(("20240212T0830", "Sydney", "Melbourne", "Adelaide"), command.params)
        
    def test_create_find_package_command(self):
        # Arrange
        input_line = "findpackage"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, FindPackageCommand)
        self.assertEqual(app_data, command.app_data)

    def test_create_view_routes_command(self):
        # Arrange
        input_line = "viewroutes"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, ViewRoutesCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)

    def test_create_check_route_command(self):
        # Arrange
        input_line = "checkroute"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, CheckRouteCommand)
        self.assertEqual(app_data, command.app_data)

    def test_create_assign_truck_command(self):
        # Arrange
        input_line = "assigntruck Man 101"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, AssignTruck)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(("Man", "101"), command.params)

    def test_create_add_pack_to_route_command(self):
        # Arrange
        input_line = "addpacktoroute 1 101"
        app_data = ApplicationData()
        cmd_factory = CommandFactory(app_data)
        # Act
        command = cmd_factory.create(input_line)
        # Assert
        self.assertIsInstance(command, AddPackToRoute)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(("1", "101"), command.params)

    
