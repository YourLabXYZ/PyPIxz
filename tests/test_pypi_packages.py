import unittest
from unittest.mock import patch, MagicMock
from src.pypixz import get_module_info
from src.pypixz.exceptions import NetworkError, JSONDecodeError


class TestPyPiPackages(unittest.TestCase):
    """Tests for `pypi_packages.py`."""

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
        self.assertEqual(result["latest_version"], "2.31.0")
        self.assertTrue(result["specific_version_exists"])

    @patch("src.pypixz._scripts.pypi_packages.requests.get")
    def test_get_module_info_module_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(NetworkError):
            get_module_info("nonexistentmodule")

    @patch("src.pypixz._scripts.pypi_packages.requests.get")
    def test_json_decode_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        with self.assertRaises(JSONDecodeError):
            get_module_info("module_with_bad_json")
