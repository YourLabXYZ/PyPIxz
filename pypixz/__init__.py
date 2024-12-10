# (c) 2024 YourLabXYZ.
# Licensed under MIT License.

""" PyPIxz

PyPIxz is a program to help developers and users to better manage
the dependencies required for the proper functioning of their program.
"""

from pypixz.install_packages import install_requirements, install_modules
from pypixz.pypi_packages import get_module_info

__version__ = '1.1.3'
__all__ = [
    'install_requirements',
    'install_modules',
    'get_module_info'
]

__author__ = 'YourLabXYZ - Organization on GitHub'
