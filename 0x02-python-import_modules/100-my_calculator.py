#!/usr/bin/python3
if __name__ == "__main__":
    """Import all functions from calculator_1.py and handle basic operations"""
    from calculator_1 import add, sub, mul, div
    import sys
    arg_len = len(sys.argv) - 1
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
