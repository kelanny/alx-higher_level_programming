#!/usr/bin/python3

"""
This module defines one function that read text files."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text, end="")
