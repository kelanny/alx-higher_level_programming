#!/usr/bin/python3
if __name__ == "__main__":
    """Import all functions from calculator_1.py and handle basic operations"""
    from calculator_1 import add, sub, mul, div
    import sys
    arg_len = len(sys.argv) - 1
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))
