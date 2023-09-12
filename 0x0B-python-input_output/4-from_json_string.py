#!/usr/bin/python3

"""
This module contains one function (from_json_string()).
The function returns an object from a JSON string.
"""


def from_json_string(my_str):
    """Returns a python object represented by a JSON string.

    Args:
        my_str (json): A JSON string to be desiarialized to python object.

    Return:
        Python object. (Python data structure).
    """

    import json
    return (json.loads(my_str))
