#!/usr/bin/python3
"""Module for print_square"""


def print_square(size):
    """print_square - print a square using #s

    Args:
        size - size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    row = "#" * size
    for i in range(size):
        print("{}".format(row))
