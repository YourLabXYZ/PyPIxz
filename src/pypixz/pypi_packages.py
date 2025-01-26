# Copyright (c) 2025 YourLabXYZ.
# Licensed under the MIT License.

import json
import requests

from .exceptions import NetworkError, JSONDecodeError


def get_module_info(module_name, version=None):
    """
    Fetch and analyze module information from the Python Package Index (PyPI).

    This function retrieves detailed information about a specified module
    from PyPI, including the module's description, latest version, and
    relevant URLs. Optionally, it verifies the existence of a specified
    version of the module. The function handles errors related to network
    issues or invalid JSON responses gracefully by raising appropriate
    exceptions when such issues occur.

    Parameters:
        module_name (str): The name of the module to fetch from PyPI.
        version (Optional[str]): The specific version of the module to check
            for existence. Defaults to None.

    Returns:
        dict: A dictionary containing the module's information, including:
            - name (str): The name of the module.
            - description (str): A summary of the module or a default message
              if not available.
            - latest_version (str): The latest version of the module.
            - project_url (str): The module's project URL, if available.
            - pypi_url (str): The PyPI URL for the module, if available.
            - specific_version_exists (bool, optional): Whether the specified
              version exists. Present only if a version parameter is provided.

    Raises:
        NetworkError: Raised for any network-related issues, including a
            404 status code or failed requests.
        JSONDecodeError: Raised when the response data cannot be decoded
            into valid JSON format.
    """

    base_url = f'https://pypi.org/pypi/{module_name}/json'

    try:
        # Make an HTTP request with a data stream (streaming)
        with requests.get(base_url, stream=True, timeout=10) as response:
            # Check immediately to avoid consuming more resources
            if response.status_code == 404:
                raise NetworkError(f"Module {module_name} not found on PyPI.")
            response.raise_for_status()  # Other HTTP errors

            # Process JSON response
            data = b"".join(response.iter_content(chunk_size=1024)).decode("utf-8").strip()

            # Check for empty response before attempting to parse
            if not data:
                raise JSONDecodeError(f"Empty response received from PyPI for module {module_name}")

            try:
                json_data = json.loads(data)  # Attempt to parse JSON
            except json.JSONDecodeError as error:
                raise JSONDecodeError(f"Invalid JSON data from PyPI: {error}") from error

            info = json_data.get("info", {})
            releases = json_data.get("releases", {})

            result = {
                "name": module_name,
                "description": info.get("summary", "No description available."),
                "latest_version": info.get("version", "Unknown"),
                "project_url": info.get("project_url", "Not available"),
                "pypi_url": info.get("package_url", "Not available"),
            }

        # Check for a specific version if provided
        if version:
            result["specific_version_exists"] = version in releases
            if not result["specific_version_exists"]:
                raise NetworkError(f"Version {version} not found for module {module_name}.")

        return result  # Return only what is needed

    except requests.RequestException as error:
        raise NetworkError(f"An error occurred while fetching data from PyPI: {error}") from error
    except ValueError as error:
        raise JSONDecodeError(f"Error decoding JSON data from PyPI: {error}") from error
