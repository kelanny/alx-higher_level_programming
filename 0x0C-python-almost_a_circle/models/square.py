#!/usr/bin/python3
# square.py

"""
The module contains one class Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class representation of  a square that inherit from Rectangle Class.

    Attributes:
        id (int): A unique integer that identify an object.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of a Rectangle Class.

        Args:
            size (int): The size of the sides of the square.
            x (int): Coordinates of x axis of the top left side of the square.
            y (int): Coordingates of y axis.
            id (int): A number that identify all instances of the Base class.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value
