#!/usr/bin/python3
# rectangle.py

"""
The module contains one class Rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """
    This class represent a rectangle.

    Attributes:
        id (int): A unique integer that identify an object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of a Rectangle Class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): Coordinates of x axis of the top left side of the rect.
            y (int): Coordingates of y axis.
            id (int): A number that identify all instances of the Base class.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the value of private attribute width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the value of private attribute width.

        Args:
            value (int): The new value of width attribute.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of private attribute height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the value of private attribute height.

        Args:
            value (int): The new value of height attribute.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be > 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the value of private attribute x."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set the value of private attribute x.

        Args:
            value (int): The new value of height attribute.

        Raises:
            TypeError: x must be an integer.
            ValueError: x must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Returns the value of private attribute y."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set the value of private attribute y.

        Args:
            value (int): The new value of y attribute.
        Raises:
            TypeError: y must be an integer.
            ValueError: y must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Returns the area of an instance of a rectangle.

        Args:
            None.
        Raises:
            None.
        Returns:
            The product of the width and the height of the rectangle object.
        """
        return (self.__width * self.__height)

    def display(self):
        """Prints the Rectangle instance to stdout with character #.

        Args:
            None.
        Raises:
            None.
        Returns:
            None
        """
        for i in range(self.__height):
            [print("#", end="") for _ in range(self.__width)]
            print("")

    def __str__(self):
        """Returns a string representation of the Rectangle instance.
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
