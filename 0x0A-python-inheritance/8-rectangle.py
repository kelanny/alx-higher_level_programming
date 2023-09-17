#!/usr/bin/python3
# 8-rectangle.py
"""
This module contain one class Rectangle.
The class inherit from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class Rectangle inherits from BaseGeometry.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize an instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """

        self.__width = width
        self.__height = height

    def integer_validator(self):
        """Validate a parameter as an integer.

        Args:
            width (): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is <= 0.
        """

        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be greater than 0")
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be greater than 0")
