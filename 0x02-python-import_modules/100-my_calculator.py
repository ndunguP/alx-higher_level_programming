#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    for j in op:
        if argv[2] == j:
            a = int(argv[1])
            b = int(argv[3])
            print("{:d} {} {:d} = {:d}".format(a, j, b, op[j](a, b)))
