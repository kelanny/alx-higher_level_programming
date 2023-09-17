#!/usr/bin/python3
# 4-inherits_from.py

"""
This  module contains one function inherits_from().
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited.

    Args:
        obj (obj): A python object.
        class (class): A python class.
    Returns:
        True: if the object is an instance of a class that inherited.
            (directly or indirectly) from the specified class.
        False:
            Otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
