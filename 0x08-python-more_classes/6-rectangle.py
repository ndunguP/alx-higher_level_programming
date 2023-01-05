#!/usr/bin/python3
"""Rectangle module for class Rectangle
   Initializes height, width, area, and parameter
"""


class Rectangle:
    """Base class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization method for width and height
        Args:
            width - width of rectangle
            height - height or rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            row = []
            for i in range(self.height):
                row += ["#" * self.width]
            return "\n".join(row)

    def __repr__(self):
        """Return a string represnetation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Delete rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
