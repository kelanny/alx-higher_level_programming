#!/usr/bin/python3
"""
The module contain a Base class.
"""


class Base:
    """This is a Base class representation.
    The class is the base of all other classes.
    It manages the id attribute in all future classes.

    Attributes:
        __nb_objects (int): Private class attribute.
        id (int): The unique id of each object related to the Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This initializes an instance of the Base class.

        Args:
            id (int): A unique integer assigned to a  base class instance.
    """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
