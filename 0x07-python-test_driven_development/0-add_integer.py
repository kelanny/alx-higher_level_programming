#!/usr/bin/python3
"""
This is 0-add_integers module.
The module supplies one function, add_integer(), for example.

>>> add_integer(10, 10)
20
"""


def add_integer(a, b=98):
    """ Returns the sum of 2 integers.

    Args:
        a (int): Integer one.
        b (int): Integer two.

    Returns:
        Sum of integers a and b.

    Raises:
        ValueError if a or b are not integers.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return (int(a) + int(b))
