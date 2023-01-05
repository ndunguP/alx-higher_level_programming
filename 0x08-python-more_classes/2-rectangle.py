#!/usr/bin/python3

'''

Rectangle class definition

'''





class Rectangle():

        '''

            Rectangle class with width and height getter/setter methods

                '''



def __init__(self, width=0, height=0):

                            self.width = width

                                    self.height = height



                                        @property

                                            def width(self):

                                                    return self.__width



                                                        @width.setter

                                                            def width(self, value):

                                                                    if type(value) is not int:

                                                                                raise TypeError("width must be an integer")

                                                                                        if value < 0:

                                                                                                    raise ValueError("width must be >= 0")

                                                                                                            self.__width = value



                                                                                                                @property

                                                                                                                    def height(self):

                                                                                                                            return self.__height



                                                                                                                                @height.setter

                                                                                                                                    def height(self, value):

                                                                                                                                            if type(value) is not int:

                                                                                                                                                        raise TypeError("height must be an integer")

                                                                                                                                                                if value < 0:

                                                                                                                                                                            raise ValueError("height must be >= 0")

                                                                                                                                                                                    self.__height = value



                                                                                                                                                                                        def area(self):

                                                                                                                                                                                                ''' calculates the area of the rectangle '''

                                                                                                                                                                                                        return self.height * self.width



                                                                                                                                                                                                            def perimeter(self):

                                                                                                                                                                                                                    ''' calculates the perimeter of the rectangle '''

                                                                                                                                                                                                                            if self.width is 0 or self.height is 0:

                                                                                                                                                                                                                                        return 0

                                                                                                                                                                                                                                                else:

                                                                                                                                                                                                                                                            return (2 * self.height) + (2 * self.width)
