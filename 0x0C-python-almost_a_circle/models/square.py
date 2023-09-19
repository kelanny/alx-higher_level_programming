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

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
