#!/usr/bin/python3
"""Module for base class base geometry and subclass rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class that inherites from Rectangle.
    Initializes size"""
    def __init__(self, size):
        """Initialize size"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Print square description"""
        class_name = self.__class__.__name__
        return "[{}] {}/{}".format(class_name, self.__size, self.__size)
