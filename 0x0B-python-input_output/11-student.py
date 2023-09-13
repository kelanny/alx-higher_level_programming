#!/usr/bin/python3

"""
This module defines a python class Student to represent a student.

"""


class Student:
    """
    A Defines a python class student.

    Attributes:
        first_name (str): Student's first name.
        last_name (str): Student's last name.
    I    age (int): Student age.
    Methods:
        __init__(self, first_name, last_name, age):
        constructur to initialize a student object.
        to_json(self, attr=None): Retrieves a dict representation of a class
    """

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of Student class.

        Args:
            first_name (str): Student first name.
            last_name (str): Student last name.
            age (int): Student age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a class object.
        If attrs is a list of str(s), represents only those attrs are included.

        Args:
            attrs (list): (Optional) The attrs to represent.
        """
        if (type(attrs) == list and all(type(item) == str for item in attrs)):
            return ({key: getattr(self, key) for key in attrs
                    if hasattr(self, key)})
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        Args:
            json (dict): a json string representation.
        """

        for key, value in json.items():
            setattr(self, key, value)
