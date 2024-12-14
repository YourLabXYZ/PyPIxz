import unittest
from unittest.mock import patch, MagicMock
from src.pypixz import install_requirements, install_modules, get_module_info


class TestInstallPackages(unittest.TestCase):
    """Tests for install_packages.py."""

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_requirements_success(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=0, stdout="Success")
        try:
            install_requirements(file_path="requirements.txt")
            mock_subprocess.assert_called_once()
        except FileNotFoundError:
            self.skipTest("requirements.txt not found; skipping test to avoid file dependencies.")

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_requirements_failure(self, mock_subprocess):
        mock_subprocess.side_effect = Exception("Installation failed")
        with self.assertRaises(EnvironmentError):
            install_requirements(file_path="requirements.txt")

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_modules_success(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=0, stdout="Success")
        self.assertTrue(install_modules(module="requests", version="2.31.0"))

    @patch("src.pypixz._scripts.install_packages.subprocess.run")
    def test_install_modules_failure(self, mock_subprocess):
        mock_subprocess.side_effect = Exception("Installation failed")
        with self.assertRaises(EnvironmentError):
            install_modules(module="nonexistentmodule")


class TestPyPiPackages(unittest.TestCase):
    """Tests for pypi_packages.py."""

    @patch("src.pypixz._scripts.pypi_packages.requests.get")
    def test_get_module_info_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "info": {"version": "2.31.0", "summary": "A test summary"},
            "releases": {"2.31.0": {}},
        }
        mock_get.return_value = mock_response
        result = get_module_info("requests", "2.31.0")
        self.assertIsInstance(result, dict)
        self.assertEqual(result["latest_version"], "2.31.0")
        self.assertTrue(result["specific_version_exists"])

    @patch("src.pypixz._scripts.pypi_packages.requests.get")
    def test_get_module_info_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        result = get_module_info("nonexistentmodule", None)
        self.assertIsInstance(result, str)
        self.assertIn("does not exist", result)


if __name__ == "__main__":
    unittest.main()
