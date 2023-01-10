#!/usr/bin/python3
""" Read a file and print to stdout """


def read_file(filename=""):
    """Read a file and print to stdout
    Args:
        filename - file to read and print
    """
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
