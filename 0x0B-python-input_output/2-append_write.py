#!/usr/bin/python3

"""
This module contains only one function (append_write()).
This function append text to files.
"""


def append_write(filename="", text=""):
    """Appends text to an existing file.
    create a new one incase the file dont exist.

    Args:
        filename (str): Name of file to append text.
        text (str): Text content to append to file.

    Return:
        Number of characters appendend to file.
    """

    char_len = len(text)
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return (char_len)
