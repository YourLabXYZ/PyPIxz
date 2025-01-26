# Preview Changelog

## [1.2.0-rc][] - 2025-01-26

### Build and Packaging

- Refactored the `install_packages.py` module to improve code readability and maintainability.
- Updated `setup.py` to include additional metadata and classifiers for better package distribution.
- Improved error handling in `install_requirements` and `install_modules` functions.

### New Features

- Introduced `get_installed_packages` function to retrieve a dictionary of installed packages and their versions.
- Added `is_package_installed` function to verify if a specific package is installed with version support.

### Bug Fixes

- Fixed an issue where `install_requirements` would fail if the requirements file contained comments or empty lines.
- Resolved a bug in `get_module_info` where network errors were not properly handled.

### Documentation

- Updated the README with new usage examples and detailed descriptions of new functions.
- Added docstrings to all functions in `install_packages.py` and `pypi_packages.py` for better code documentation.

### Testing

- Added comprehensive unit tests for `install_requirements`, `install_modules`, `get_installed_packages`, and `is_package_installed` functions.
- Improved test coverage for exception handling scenarios.
## [1.2.0-preview.4][] - 2024-12-28

### Build and Packaging

- Modified `BasePyPIxzException` to allow detailed error messages with an
optional `details` argument for better error
tracking.
- Major improvements to the `install_requirements` function:
  - Preloads already installed dependencies to avoid duplicates.
  - Enhanced error handling with more detailed and user-friendly messages.
  - Updated documentation for parameters and possible exceptions.
- Added new utility functions:
  - `get_installed_packages`: Retrieves a dictionary of installed packages and
  their versions.
  - `is_package_installed`: Verifies if a specific package is installed
  (with version support).

### Miscellaneous Fixes

- Adjusted imports in `__init__.py` to reflect refactored and removed components.

### Testing

- Added a new file to be able to test all the program's functionalities.

## [1.2.0-preview.3][] - 2024-12-17

### Testing Enhancements

- Added unit tests to validate:
  - Retrieval of module information using `get_module_info`, including success and failure scenarios.
  - Custom exception handling, such as `NetworkError`, `JSONDecodeError`, and others.
  - Methods for installing modules and dependency files, covering both success and failure cases.

## [1.2.0-preview.2][] - 2024-12-10

### Exceptions and Error Handling

- Introduced a new exceptions module (`exceptions.py`) to centralize exception handling within the project:
  - Added base exception classes such as `BasePyPIxzException` and more specific error categories: 
    `NetworkError`, `DependencyError`, `FileError`, etc.
  - Enhanced error granularity for dependency and network-related issues like 
    `MissingRequirementsFileError`, `ModuleInstallationError`, and `TimeoutError`.

- Refactored `install_packages.py` to integrate centralized exceptions to improve error reporting and diagnostics.

### Networking and Module Information

- Improved `pypi_packages.py` to utilize exception classes for managing network and JSON decoding errors.

- Added robust error checking in `get_module_info()` to identify and handle specific cases of module version unavailability on PyPI.

### Build and Packaging Improvements

- Enhanced the modular organization of the codebase by decoupling exception handling and core functionality.
- Removed deprecated `install_packages.py` script for an improved module structure.
- Updated project version to `1.2.0-preview.2` in all configuration files.
- Introduced `src/pypixz/__version__.py` to centralize version and metadata information.

### Testing

- Added a comprehensive test suite (`tests.py`) using `unittest` and `unittest.mock`.

### Documentation and Module Structure

- Published an improved module-level docstring in `src/pypixz/__init__.py`.
- Streamlined module organization by relocating and restructuring components.

## [1.2.0-preview.1][] - 2024-12-09

### Build and Packaging Improvements

- Adding a timeout to the `requests.get` method
([#44](https://github.com/YourLabXYZ/PyPIxz/issues/44))

### Documentation and Help Content

- Fixed punctuation problem.
([#51](https://github.com/YourLabXYZ/PyPIxz/issues/51))
- Fixing the file in Markdown format.
([#50](https://github.com/YourLabXYZ/PyPIxz/issues/50))
- Fixed issue with using dollar sign.
([#49](https://github.com/YourLabXYZ/PyPIxz/issues/49))
- Fixed space issue in Markdown format files.
([#48](https://github.com/YourLabXYZ/PyPIxz/issues/48))
- Specifying a code block language
([#47](https://github.com/YourLabXYZ/PyPIxz/issues/47))
- Lists surrounded by empty lines
([#46](https://github.com/YourLabXYZ/PyPIxz/issues/46))
- Reduced the number of characters in lines in Markdown files
([#45](https://github.com/YourLabXYZ/PyPIxz/issues/45))

[1.2.0-rc]: https://github.com/YourLabXYZ/PyPIxz/compare/v1.2.0-preview.4...v1.2.0-rc
[1.2.0-preview.4]: https://github.com/YourLabXYZ/PyPIxz/compare/v1.2.0-preview.3...v1.2.0-preview.4
[1.2.0-preview.3]: https://github.com/YourLabXYZ/PyPIxz/compare/v1.2.0-preview.2...v1.2.0-preview.3
[1.2.0-preview.2]: https://github.com/YourLabXYZ/PyPIxz/compare/v1.2.0-preview.1...v1.2.0-preview.2
[1.2.0-preview.1]: https://github.com/YourLabXYZ/PyPIxz/compare/v1.1.3...v1.2.0-preview.1
