# (c) 2024 YourLabXYZ.
# Licensed under MIT License.

import requests


def get_module_info(module_name, version=None):
    """
    Retrieves information about a module from PyPI.

    :param module_name: The name of the module to search for.
    :param version: A specific version to check. Default is None.

    :return: Information about the module or an error message.
    """

    base_url = f'https://pypi.org/pypi/{module_name}/json'

    try:
        # Make a request to the PyPI API to fetch module data
        response = requests.get(base_url, timeout=10)
        if response.status_code == 404:
            return f"The module '{module_name}' does not exist on PyPI."

        data = response.json()
        info = data.get("info", {})
        releases = data.get("releases", {})

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
                return f"Version {version} is not available."

        return result

    except requests.RequestException as error:
        return f"A network error occurred: {error}"
    except ValueError as error:
        return f"A value error occurred: {error}"

# Example call (disabled to prevent immediate execution)
# module_info = get_module_info("requests", "2.26.0")
# print(module_info)