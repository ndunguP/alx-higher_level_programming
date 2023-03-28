#!/usr/bin/python3
class Square:
    """A Square class.
    Initializes the size of the square, gets and sets the size, returns
    the area of the square
    """

    def __init__(self, size=0):
        """Initialize size of sqaure."""
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return area of square."""
        return self.__size ** 2
