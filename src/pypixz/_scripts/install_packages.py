# Copyright (c) 2025 YourLabXYZ.
# Licensed under the MIT License.

import os
import logging
import subprocess
import sys

from .pypi_packages import get_module_info
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

        with open(file_path, "r", encoding="utf-8") as file:
            required_packages = [line.strip() for line in file.readlines() if line.strip()]

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


def install_modules(module, version=None, version_range=None, enable_logging=False):
    """
    Install a specified Python module with optional version, version range, and logging.

    This function allows for installing a Python module from PyPI, with the option to specify
    a specific version, version range, or using the latest available version. It supports
    logging for debugging purposes and handles various error scenarios like dependency issues
    or installation failure.

    Parameters:
        module: str
            The name of the module to be installed.
        version: str, optional
            The specific version of the module to be installed. Defaults to None.
        version_range: str, optional
            A version range specifier if a specific range of versions is needed.
            Defaults to None.
        enable_logging: bool, optional
            Whether to enable logging for the installation process. If True, logging
            information will be captured. Defaults to False.

    Raises:
        ModuleInstallationError:
            Raised when the module installation fails due to system issues, dependency
            issues, or other reasons.
        DependencyError:
            Raised when the requested version or version range is incompatible or not
            available on PyPI.

    Returns:
        bool
            True if the module was installed successfully.
    """

    try:
        # Retrieve module information for validation (via PyPI)
        module_info = get_module_info(module)

        # If a specific version is requested, check it
        if version:
            if version not in module_info.get("release", {}):
                raise DependencyError(f"The version {version} of the module {module} cannot be found on PyPI.")

        # Format the package with a version or version range
        if version:
            package_specifier = f"{module}=={version}"
        elif version_range:
            package_specifier = f"{module}{version_range}"  # e.g. "module>=1.2.0, !=2.0.0"
        else:
            package_specifier = module  # Latest version installed by default

        # Pip command with specifier
        command = [
            sys.executable, "-m", "pip", "install", package_specifier
        ]

        # Call pip install
        result = subprocess.run(
            command,
            check=True,  # Raises CalledProcessError if the command fails
            capture_output=True,  # Captures stdout and stderr for debugging/logging
            text=True  # Decodes stdout/stderr as text
        )

        success_message = f"Module {module} successfully installed."
        logging.info(success_message) if enable_logging else print(success_message)

        # Optionally log the output for debugging
        if enable_logging:
            logging.debug("Command output:\n%s", result.stdout)

        return True

    except subprocess.CalledProcessError as error:
        error_message = (f"An error occurred while installing the module {module}: "
                         f"{error.stderr or 'Unknown error'}")
        logging.error(error_message) if enable_logging else print(error_message)
        raise ModuleInstallationError(error_message) from error

    except (OSError, DependencyError) as dep_error:
        message = f"System or dependency error for the module {module}: {dep_error}"
        logging.error(message) if enable_logging else print(message)
        raise ModuleInstallationError(message) from dep_error
