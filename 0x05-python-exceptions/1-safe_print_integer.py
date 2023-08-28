#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer.

    Args:
        Value: The element to print.
    Returns:
        Returns True if integer, else returns False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
