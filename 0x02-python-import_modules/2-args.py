#!/usr/bin/python3
if __name__ == "__main__":
    """Prints list of commandline arguments."""
    import sys
    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:\n{}: {}".format(arg_len, 1, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_len))
        for i in range(arg_len):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
