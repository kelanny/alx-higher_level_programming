#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """ Intantiate a new square.

        Args:
            size (int): The size of the sides of the square.
            position (int, int): An optional position of the new square.
        """
        self.size = size
        self.position = position

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
    
    @property
    def position(self):
        """Get or set the current square position."""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of (x, y)")
        self.__position = value

    def area(self):
        """ Returns the area of a the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with using #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
