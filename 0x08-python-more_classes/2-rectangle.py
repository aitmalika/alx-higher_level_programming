#!/usr/bin/python3
"""
Define this Rectangle class
"""


class Rectangle:
    """ Rectangles """
    def __init__(self, width=0, height=0):
        """ initizie with and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ with get ter """
        return self.__width

    @width.setter
    def width(self, value):
        """ with set ter """
        if type(value) is not int:
            raise TypeError("with most be an integer")
        if value < 0:
            raise ValueError("with most be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height get ter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height set ter """
        if type(value) is not int:
            raise TypeError("height most be an integer")
        if value < 0:
            raise ValueError("height most be >= 0")
        self.__height = value

    def area(self):
        """ calculate and return this area """
        return self.__width * self.__height

    def perimeter(self):
        """ calculate the perimetere of this Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
