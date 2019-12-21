#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    i = int(sys.argv[1])
    j = int(sys.argv[3])

    if sys.argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(i, j, add(i, j)))
    elif sys.argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(i, j, sub(i, j)))
    elif sys.argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(i, j, mul(i, j)))
    elif sys.argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(i, j, div(i, j)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
