# Preview Changelog

## [1.2.0-preview.2][] - 2024-12-10

### Build and Packaging Improvements

- Removed deprecated `install_packages.py` script for an improved module structure.
- Updated project version to `1.2.0-preview.2` in all configuration files.

### New Features

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

[1.2.0-preview.2]: https://github.com/YourLabXYZ/PyPIxz/compare/master...release/v1.2
[1.2.0-preview.1]: https://github.com/YourLabXYZ/PyPIxz/compare/v1.1.3...v1.2.0-preview.1
