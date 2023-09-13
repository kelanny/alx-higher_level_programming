#!/usr/bin/python3
"""
This module defines a class-to-json serialization function.
"""


def class_to_json(obj):
    """returns a dictionary description of simple data structure.

    Args:
        obj (obj): The object to serialize.

    Return:
        Dictionary description of an object (obj).
    """
    return (obj.__dict__)
