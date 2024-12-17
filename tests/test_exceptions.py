import unittest
from src.pypixz.exceptions import (
    MissingRequirementsFileError, ModuleInstallationError, NetworkError, JSONDecodeError
)


class TestExceptions(unittest.TestCase):
    """Tests for exception classes in PyPIxz."""

    def test_missing_requirements_file_error(self):
        with self.assertRaises(MissingRequirementsFileError):
            raise MissingRequirementsFileError("Requirements file is missing.")

    def test_module_installation_error(self):
        with self.assertRaises(ModuleInstallationError):
            raise ModuleInstallationError("Failed to install module.")

    def test_network_error(self):
        with self.assertRaises(NetworkError):
            raise NetworkError("Failed due to a network error.")

    def test_json_decode_error(self):
        with self.assertRaises(JSONDecodeError):
            raise JSONDecodeError("Failed decoding invalid JSON.")
