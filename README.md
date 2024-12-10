# PyPIxz

**PyPIxz** is a simple, modern, and easy-to-use solution for managing your Python dependencies.

```python
import pypixz

# Install dependencies listed in a requirements.txt file
pypixz.install_requirements("requirements.txt", enable_logging=False)

# Retrieve information from a module.
result = pypixz.get_module_info("pypixz", version="1.1.2")
print(result)
```

Output result of `get_module_info` command :

```
{'name': 'pypixz', 'description': 'PyPIxz is a simple, modern, and easy-to-use solution for managing your Python dependencies.', 'latest_version': '1.1.2', 'project_url': 'https://pypi.org/project/PyPIxz/', 'pypi_url': 'https://pypi.org/project/PyPIxz/', 'specific_version_exists': True}
```

> [!TIP]
> If you need a much lighter version for specific needs you can use our [LITE version](https://github.com/YourLabXYZ/PyPIxz-LITE).

> [!WARNING]
> We recommend using PyPIxz LITE at the very beginning of your program to avoid running into the
> `ModuleNotFoundError` error.

PyPIxz allows you to easily and simply manage the dependencies necessary for your Python program while maintaining a certain security. It is designed to be compatible with other internal modules such as **logging** for log management while ensuring compatibility with any Python environment from version 3.8.

[![Contributors](https://img.shields.io/github/contributors/yourlabxyz/PyPIxz.svg)](https://github.com/yourlabxyz/PyPIxz/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/yourlabxyz/PyPIxz.svg)](https://github.com/yourlabxyz/PyPIxz/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/yourlabxyz/PyPIxz.svg)](https://github.com/yourlabxyz/PyPIxz/pulls)
[![Forks](https://img.shields.io/github/forks/yourlabxyz/PyPIxz.svg)](https://github.com/yourlabxyz/PyPIxz/network/members)

---

## Installing PyPIxz and Supported Versions

PyPIxz is available on PyPI:

```console
python -m pip install pypixz
```

PyPIxz officially supports **Python 3.8+** : 

> [!CAUTION]
> You can use PyPIxz with a version of Python lower than 3.8, but we do not guarantee the
> compatibility of the program or its updates or security.

---

## Supported Features & Best–Practices

PyPIxz is ready to meet the requirements of managing your dependencies in a robust and reliable way, for today's needs.

- **Fast Installation**: Manage your dependencies from a `requirements.txt` file.
- **Modularity**: Compatible with other tools and libraries, such as `logging`.
- **Broad Compatibility**: Supports modern Python versions (3.8+).
- **Check Module Information:** Retrieves various information about the modules you want.

## License

This project is licensed under the [MIT License](https://github.com/yourlabxyz/PyPIxz/blob/master/LICENSE). See 
the license file for more details.

---
