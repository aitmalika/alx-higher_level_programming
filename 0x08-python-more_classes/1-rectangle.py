#!/usr/bin/python3
"""
Define Rectangles this class
"""


class Rectangle:
    """ Rectangles """
    def __init__(self, width=0, height=0):
        """ initizie with this height """
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
