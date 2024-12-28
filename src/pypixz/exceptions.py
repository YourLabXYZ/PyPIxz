# Copyright (c) 2024 YourLabXYZ.
# Licensed under the MIT License.

class BasePyPIxzException(Exception):
    """Base exception for PyPIxz."""

    def __init__(self, *args, details=None, **kwargs):
        """
        Initialize the exception with optional additional arguments.
        """
        self.details = details  # Stores the additional details
        super().__init__(*args)  # Passes the positional arguments to Exception


# Exceptions for dependency management and package installation
class DependencyError(BasePyPIxzException):
    """Exception raised when a dependency cannot be installed."""


class MissingRequirementsFileError(DependencyError):
    """Exception raised when a requirements file is missing."""


class ModuleInstallationError(DependencyError):
    """Exception raised when a module cannot be installed."""


class InvalidModuleVersionError(DependencyError):
    """Exception raised when a module version is invalid."""


# Exceptions for networking
class NetworkError(BasePyPIxzException):
    """Exception raised when there is a network error."""


class TimeoutError(NetworkError):
    """Exception raised when a request times out."""


class ConnectionError(NetworkError):
    """Exception raised when a connection error occurs."""


# Exceptions for JSON
class JSONError(BasePyPIxzException):
    """Exception raised when there is a JSON error."""


class JSONDecodeError(JSONError):
    """Exception raised when JSON decoding fails."""


class InvalidJSONResponseError(JSONError):
    """Exception raised when the JSON response is invalid."""


# Additional utility exceptions
class FileError(BasePyPIxzException):
    """Exception raised when there is a file error."""


class ChunkedEncodingError(FileError):
    """Exception raised when chunked encoding fails."""


class SteamConsumeError(FileError):
    """Exception raised when Steam consume fails."""


# Example of Warning (if needed later)
class PyPIxzWarning(Warning):
    """Base warning for PyPIxz."""


class DeprecatedFeatureWarning(PyPIxzWarning):
    """Warning for deprecated features."""
