#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Base class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization method for width and height
        Args:
            width - width of rectangle
            height - height or rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
