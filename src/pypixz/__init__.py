# Copyright (c) 2024 YourLabXYZ.
# Licensed under the MIT License.

"""
PyPIxz module to manage your dependencies.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyPIxz module to manage your dependencies in a simple and efficient way while maintaining guaranteed security.
Basic usage:
    import pypixz

    pypixz.install_requirements("requirements.txt", enable_logging=False)

    result = pypixz.get_module_info("pypixz", version="1.1.2")
    print(result)

:copyright: (c) 2024 YourLabXYZ.
:license: MIT, see LICENSE for more details.
"""

__all__ = [
    'install_requirements',
    'get_module_info'
]

from .__version__ import (
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __license__,
    __copyright__
)

from ._scripts.install_packages import install_requirements
from ._scripts.pypi_packages import get_module_info
