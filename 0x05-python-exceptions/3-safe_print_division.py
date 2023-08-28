#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide 2 integers and print the result.

    Args:
        a(int): First integer.
        b(int): Second integer.
    Returns:
        Value of division or None.
    """
    try:
        quontient = a / b
    except (TypeError, ZeroDivisionError):
        quontient = None
    finally:
        print("Inside result: {}".format(quontient))
    return (quontient)
