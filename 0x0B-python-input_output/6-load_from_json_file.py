#!/usr/bin/python3

"""
This module contains one function (load_from_json_file()).
It loads JSON strings representations into python objects.
"""


def load_from_json_file(filename):
    """Creates a python object from JSON file.

    Args:
        filename (str): Name of the JSON file to read.
    """
    import json
    with open(filename, 'r', encoding="utf-8") as file:
        obj_str = file.read()
        return (json.loads(obj_str))
