#!/usr/bin/python3
""" Module for class that inherits from int"""


class MyInt(int):
    """Class that inherits from int"""
    def __init__(self, value):
        """Initialize value"""
        self.value = value

    def __eq__(self, other):
        """Equals method, change to not equals"""
        return self.value != other

    def __ne__(self, other):
        """Not equals method, change to equals"""
        return self.value == other
