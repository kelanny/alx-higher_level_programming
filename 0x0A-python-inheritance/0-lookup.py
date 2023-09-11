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
    attr_and_mthds = dir(obj)
    fil_att_n_mthds = [att for att in attr_and_mthds if not att.startswith("_")]
    return (fil_att_n_mthds)
