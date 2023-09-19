#!/usr/bin/python3
"""
The module contain a Base class.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a json string representation of list with Base class instanses

        Args:
            list_objs (list): A list of inherited class instances.
        """

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [item.to_dictionary() for item in list_objs]
                jfile.write(Base.to_json_string(list_dicts))
