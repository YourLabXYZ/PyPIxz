# Copyright (c) 2024 YourLabXYZ.
# Licensed under the MIT License.

import os
import logging
import subprocess
import sys

from ..exceptions import (
    MissingRequirementsFileError,
    ModuleInstallationError,
    DependencyError
)


def install_requirements(file_path="requirements.txt", enable_logging=False):
    """
    Install required Python packages from a requirements file.

    This function enables the installation of Python package dependencies defined
    in a requirements file. It first checks the file's existence before validating
    if all required packages are already installed. If some packages aren't
    installed, it executes `pip` to install the missing dependencies. The function
    includes optional logging features to record status, success, or error messages.

    Parameters:
        file_path (str): The path to the requirements file. Defaults to
            "requirements.txt".
        enable_logging (bool): Flag to enable or disable logging. Defaults to False.

    Raises:
        MissingRequirementsFileError: If the specified requirements file does not
            exist or cannot be accessed.
        ModuleInstallationError: If an error occurs during the module installation
            using pip.
        DependencyError: If an OS-level error occurs during the installation
            process.
    """

    file_path = os.path.abspath(file_path)

    # Check if the file exists and is valid
    if not os.path.isfile(file_path):
        message = f"The {file_path} file was not found."
        logging.error(message) if enable_logging else print(message)
        raise MissingRequirementsFileError(message)

    try:
        # Preloading existing packages to avoid installing duplicates.
        existing_packages = get_installed_packages()

        with open(file_path, "r") as f:
            required_packages = [line.strip() for line in f.readlines() if line.strip()]

        # Filter packages that require installation
        packages_to_install = [
            pkg for pkg in required_packages if not is_package_installed(pkg, existing_packages)
        ]

        if not packages_to_install:
            success_message = "All dependencies are already installed."
            logging.info(success_message) if enable_logging else print(success_message)
            return


        # Build pip command
        command = [
            sys.executable, "-m", "pip", "install", "--no-cache-dir", "--no-deps",
            *packages_to_install
        ]

        result = subprocess.run(
            command,
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
        raise ModuleInstallationError(error_message) from error

    except OSError as os_error:
        message = f"OS error occurred during installation: {os_error}"
        logging.error(message) if enable_logging else print(message)
        raise DependencyError(message) from os_error


def get_installed_packages():
    """
    Retrieves a dictionary of installed Python packages along with their versions.

    The function executes the `pip freeze` command to obtain a list of installed
    packages and their respective versions. It then parses the output, extracting
    the package names and their versions, and stores them in a dictionary where
    the keys are package names in lowercase, and the values are the corresponding
    versions.

    Raises:
        subprocess.CalledProcessError: If the `pip freeze` command execution fails.

    Returns:
        dict: A dictionary containing installed package names as keys (in lowercase)
        and their corresponding versions as values.
    """

    installed_packages = {}
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        check=True,  # Raises CalledProcessError if the command fails
        capture_output=True,  # Captures stdout and stderr for debugging/logging
        text=True  # Decodes stdout/stderr as text
    )

    for line in result.stdout.split("\n"):
        if "==" in line:
            name, version = line.split("==")
            installed_packages[name.lower()] = version
    return installed_packages


def is_package_installed(package_line, installed_packages):
    """
    Check if a package is installed in the given list of installed packages.

    This function determines whether a provided package from a package_line
    is installed by checking the installed_packages dictionary. It accounts
    for both specific version requirements and general presence of the
    package.

    Parameters:
        package_line (str): A string representing the package, potentially
        including a required version, e.g., "package_name==1.0.0".

        installed_packages (dict[str, str]): A dictionary representing the
        currently installed packages. Keys are lowercase package names and
        values are their installed versions.

    Returns:
        bool: True if the package is installed with required version (if
        specified), or if the package is found installed without-version
        specification. False otherwise.
    """

    if "==" in package_line:
        name, required_version = package_line.split("==")
        return installed_packages.get(name.lower()) == required_version
    return package_line.lower() in installed_packages
