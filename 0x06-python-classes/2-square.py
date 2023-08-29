#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """ Intantiate a square class.

        Args:
            size (int): The size of the sides of the square.
        """

        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
