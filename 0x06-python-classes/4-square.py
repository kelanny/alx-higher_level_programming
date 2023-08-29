#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """ Intantiate a new square.

        Args:
            size (int): The size of the sides of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Change the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of a the square."""
        return (self.__size * self.__size)
