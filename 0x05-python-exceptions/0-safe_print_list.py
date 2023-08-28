#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    Args: 
        my_list(list): The list containing the elements.
        x(int): No of elements to print.

    Returns:
        The actual number of elements printed.
    """
    items = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            items += 1
        except IndexError:
            break
    print()
    return (items)
