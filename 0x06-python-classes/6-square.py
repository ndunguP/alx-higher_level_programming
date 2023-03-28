#!/usr/bin/python3
class Square:
    """"A Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Intialize size and position of square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """"Setter for square size."""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for square position."""
        if ((type(value) is not tuple) or
                (len(value) != 2) or
                (type(value[0]) is not int) or
                (type(value[1]) is not int) or
                (value[0] < 0) or
                (value[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Calculate and return area of square."""
        return self.__size ** 2

    def my_print(self):
        """"Print the square to stdout."""
        if self.size <= 0:
            print()
        else:
            row = ' ' * self.position[0]
            row += "#" * self.size
            for k in range(self.position[1]):
                print("")
            for i in range(self.size):
                print("{}".format(row))
