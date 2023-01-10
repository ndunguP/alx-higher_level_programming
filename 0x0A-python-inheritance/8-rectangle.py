#!/usr/bin/python3
"""Module for base class base geometry and subclass rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherites from BaseGeometry.
    Intializes width and height"""
    def __init__(self, width, height):
        """Method to initialize width and height"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
