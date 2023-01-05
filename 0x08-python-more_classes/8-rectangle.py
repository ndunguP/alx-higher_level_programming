#!/usr/bin/python3
"""Rectangle module for class Rectangle
   Initializes height, width, area, and parameter
"""


class Rectangle:
    """Base class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

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
                row += [str(self.print_symbol) * self.width]
            return "\n".join(row)

    def __repr__(self):
        """Return a string represnetation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Delete rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
