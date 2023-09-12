#!/usr/bin/python3

"""
This module contains one function (to_json_string()).
The function returns a JSON representation of the object.
"""


def to_json_string(my_obj):
    """Returns JSON representation of an object.

    Args:
        myobj (obj): The object to be represented in JSON.

    Return:
        JSON string representation.
    """

    import json
    return (json.dumps(my_obj))
