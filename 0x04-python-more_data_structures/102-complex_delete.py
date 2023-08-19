#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    if value is None:
        return (a_dictionary)
    key_list = list(a_dictionary.keys())
    for key in key_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return (a_dictionary)
