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
        """Return a dictionary representation of a class object."""
        return (self.__dict__)
