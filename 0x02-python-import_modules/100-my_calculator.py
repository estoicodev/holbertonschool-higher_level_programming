#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    calc = sys.argv[2]
    b = int(sys.argv[3])

    if calc == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif calc == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif calc == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif calc == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
