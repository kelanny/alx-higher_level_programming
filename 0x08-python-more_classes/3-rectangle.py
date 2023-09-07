#!/usr/bin/python3
"""Creates an empty class Rectangle."""


class Rectangle:
    """Defines an empty class rectangle."""

    def __init__(self, width=0, height=0):
        """Initiate a rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The heigit of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        _area = self.__width * self.__height
        return (_area)

    def perimeter(self):
        """Returns the perimeter of the rectaingle."""
        if self.__width == 0 or self.__height == 0:
            _perimeter = 0
        _perimeter = 2 * (self.__width + self.__height)
        return (_perimeter)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return (rect_str)
