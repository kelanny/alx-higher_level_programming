#!/usr/bin/python3

"""
This module contains one function save_to_json_file().
The function writes an object to text file using JSON.
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON.

    Args:
        my_obj (obj): The object to write to a file.
        filename (str): The filename to write to.
    """

    import json
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
