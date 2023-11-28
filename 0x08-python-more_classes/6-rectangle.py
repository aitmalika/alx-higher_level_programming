#!/usr/bin/python3
"""
Defines Rectangle this class
"""


class Rectangle:
    """ Rectangles """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initialise """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ return set of this rectangle """
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
        return "Rectangl({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del """
        print("Bye rectangl...")
        Rectangle.number_of_instances -= 1

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
