#!/usr/bin/python3
"""
Define this Rectangles class
"""


class Rectangle:
    """ Rectangles """
    def __init__(self, width=0, height=0):
        """ initialise """
        self.width = width
        self.height = height

    def __str__(self):
        """ return set of rectangles """
        if self.__height == 0 or self.__width == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += '#'
            ret += '\n'
        return ret[:-1]

    def __repr__(self):
        """ repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

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
        """ calculate area of this rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculate the perimeter of this rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
