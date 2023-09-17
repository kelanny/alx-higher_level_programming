#!/usr/bin/python3

"""
This module defines one fuction (lookup()).

"""


def lookup(obj):
    """returns a list of available attributes and methods of an object.
    Args:
        obj (obj): The object to check for attributes.
    Return:
        A list of all methods and attributes of an object.
    """
    return (dir(obj))
