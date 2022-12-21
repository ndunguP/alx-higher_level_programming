#!/usr/bin/python3
'''
Square class definition
'''


class Square():
    '''
    Square class with private attribute size
    '''
    def __init__(self, size=0):
        '''
        Args:
            size: size of the square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        return self.__size * self.__size
