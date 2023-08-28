#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Arg:
        my_list_1(list): List one.
        my_list_2(list): List 2.
    Returns:
        Returns a new list with all the division.
    """
    division_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            break
        finally:
            division_list.append(result)
    return (division_list)
