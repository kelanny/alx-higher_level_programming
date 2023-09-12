#!/usr/bin/python3

"""
This module contains one function (write_file()) which write text to files.
"""


def write_file(filename="", text=""):
    """Writes text to a file named (filename)

    Args:
        filename (str): Name of the file to write.
        text (str): Text content to write.

    Return:
        Number of characters writen to the file.

    """
    char_len = len(text)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

    return (char_len)
