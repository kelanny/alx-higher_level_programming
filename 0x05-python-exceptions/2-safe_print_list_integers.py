#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints first x elements of alist and only integers.

    Args:
        my_list(list): The list containing elements to print.
        x(int): the number of elements to print in a list.
    Returns:
        Actual no of integers printed.
    """
    elems = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elems += 1
        except IndexError:
            break
        except (TypeError, ValueError):
            continue
    print("")
    return (elems)
