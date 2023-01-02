#!/usr/bin/python3
"""Module to print string"""


def say_my_name(first_name, last_name=""):
    """say_my_name - print string
    
    Args:
        first_name - first name to print
        last_name - last name to print
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
