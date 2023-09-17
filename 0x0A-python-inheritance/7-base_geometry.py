#!/usr/bin/python3
# 6-base_geometry.py

"""
This module contains an empty class BaseGeometry.
"""


class BaseGeometry:
    """An empty Base class representation of BaseGeometry.

    Attributes:
        None.
    """

    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str): Will always be a string.
            value (int): Must be an integer.
        Raises:
            TypeError: if value not integer.
            ValueError: If value <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
