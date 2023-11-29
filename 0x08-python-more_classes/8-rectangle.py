#!/usr/bin/python3
"""
Defines Rectangle this class
"""


class Rectangle:
    """ Rectangle """

    number_of_instances = 0
    print_symbol = '#'

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
                ret += str(self.print_symbol)
            ret += '\n'
        return ret[:-1]

    def __repr__(self):
        """ repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ width get ter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width set ter """
        if type(value) is not int:
            raise TypeError("with must be an integer")
        if value < 0:
            raise ValueError("with must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height get ter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates area of this rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of this rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger_or_equal """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of this Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of  THIS Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
