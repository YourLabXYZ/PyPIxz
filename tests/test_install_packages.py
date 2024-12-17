import unittest
from unittest.mock import patch, MagicMock
import subprocess
from src.pypixz import install_requirements, install_modules
from src.pypixz.exceptions import MissingRequirementsFileError, ModuleInstallationError


class TestInstallPackages(unittest.TestCase):
    """Tests for `install_packages.py` methods."""

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_requirements_success(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=0, stdout="Success")
        install_requirements(file_path="requirements.txt")
        mock_subprocess.assert_called_once_with(
            [subprocess.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
            capture_output=True,
            text=True
        )

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_requirements_missing_file(self, mock_subprocess):
        with self.assertRaises(MissingRequirementsFileError):
            install_requirements(file_path="nonexistent_requirements.txt")

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_modules_success(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=0, stdout="Success")
        result = install_modules("requests", version="2.31.0")
        self.assertTrue(result)

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_modules_failure(self, mock_subprocess):
        mock_subprocess.side_effect = subprocess.CalledProcessError(1, "cmd")
        with self.assertRaises(ModuleInstallationError):
            install_modules("invalidmodule")
