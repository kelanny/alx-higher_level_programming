#!/usr/bin/python3
"""
This is a 3-say_my_name module.
It defines one function say_my_name().

"""


def say_my_name(first_name, last_name=""):
    """It prints first and last name.

    Args:
        first_name (str): First argument.
        last_name (str): Last argument.

    Raises:
        TypeError: exception where first_name or last name are not strings.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string.")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string.")
    print("My name is {} {}".format(first_name, last_name))
