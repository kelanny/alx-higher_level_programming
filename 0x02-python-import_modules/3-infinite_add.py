#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the sum of all arguments."""
    import sys
    arg_len = len(sys.argv) - 1
    total = 0
    if arg_len == 0:
        print("{}".format(total))
    else:
        for i in range(arg_len):
            total += int(sys.argv[i + 1])
        print("{}".format(total))
