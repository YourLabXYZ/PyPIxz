# Copyright (c) 2024 YourLabXYZ.
# Licensed under the MIT License.

import os
import logging
import subprocess
import sys

from .pypi_packages import get_module_info


def install_requirements(file_path="requirements.txt", enable_logging=False):
    """
    Installs all packages listed in a requirements.txt file.

    :param file_path: Path to the requirements.txt file (default is "requirements.txt").
    :param enable_logging: Enable logging (default is False).
    """

    file_path = os.path.abspath(file_path)

    # Check if the file exists and is valid
    if not os.path.isfile(file_path):
        message = f"The {file_path} file was not found."
        logging.error(message) if enable_logging else print(message)
        raise FileNotFoundError(message)

    try:
        # Run the pip install -r requirements.txt command
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", file_path],
            check=True,  # Raises CalledProcessError if the command fails
            capture_output=True,  # Captures stdout and stderr for debugging/logging
            text=True  # Decodes stdout/stderr as text
        )

        success_message = "Successfully installed dependencies."
        logging.info(success_message) if enable_logging else print(success_message)

        # Optionally log the output for debugging
        if enable_logging:
            logging.debug("Command output:\n%s", result.stdout)

    except subprocess.CalledProcessError as error:
        # Handle installation errors
        error_message = (f"An error occurred while installing dependencies: "
                         f"{error.stderr or 'Unknown error'}")
        logging.error(error_message) if enable_logging else print(error_message)
        raise EnvironmentError(error_message) from error

# Example usage (disabled to prevent immediate execution)
# install_requirements("requirements.txt")


def install_modules(module, version=None, latest_version=True, enable_logging=False):
    """
    Installs a specific version of a Python module using subprocess.

    :param module: The name of the module to install.
    :param version: The version of the module to install.
    :param latest_version: Installs the latest version of the module if no version specified
                           (default is True).
    :param enable_logging: Enable logging (default is False).
    """

    module_info = get_module_info(module, version if version is not None else None)


    if not isinstance(module_info, str):
        if version is None and latest_version:
            version = module_info['latest_version']

        try:
            # Run the pip install {module} or {module}>={version} command
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install",
                 f"{module}>={version}" if version is not None else f"{module}"],
                check=True,  # Raises CalledProcessError if the command fails
                capture_output=True,  # Captures stdout and stderr for debugging/logging
                text=True  # Decodes stdout/stderr as text
            )

            success_message = "Successfully installed module."
            logging.info(success_message) if enable_logging else print(success_message)

            # Optionally log the output for debugging
            if enable_logging:
                logging.debug("Command output:\n%s", result.stdout)

            return True

        except subprocess.CalledProcessError as error:
            # Handle installation errors
            error_message = (f"An error occurred while installing module: "
                             f"{error.stderr or 'Unknown error'}")
            logging.error(error_message) if enable_logging else print(error_message)
            raise EnvironmentError(error_message) from error
    else:
        logging.error(module_info) if enable_logging else print(module_info)
        raise EnvironmentError(module_info)

# Example usage (disabled to prevent immediate execution)
# install_module("requests", "2.26.0")
