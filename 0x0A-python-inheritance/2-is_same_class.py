#!/usr/bin/python3
# 2-is_same_class.py
"""
This module contains a function is_same_class().
It returns true if obj is an instance of specified class.
"""


def is_same_class(obj, a_class):
    """Return true if obj is instance of a_class.

    Args:
        obj (obj): A python object.
        a_class (class): A python class

    Returns:
        True: if obj is instance of a_class.
        False: if not an instance.
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
