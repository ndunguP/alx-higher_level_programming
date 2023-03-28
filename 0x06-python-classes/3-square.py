#!/usr/bin/python3
class Square:
    """A Square class"""
    def __init__(self, size=0):
        """Initialize a private attribute to size if conditions are met."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        "Public method that calculates and returns the current square area."""
        return self.__size ** 2
