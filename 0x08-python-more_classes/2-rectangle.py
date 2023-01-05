#!/usr/bin/python3
"""Rectangle module for class Rectangle
   Initializes height, width, area, and parameter
"""


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
        """Setter for rectangle width
            value must be a positive integer
        """
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
        """Setter for rectangle height
           value must be a positive integer
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method that returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method to return parimeter of rectangle
           If width or height is zero, perimeter is equal to 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
