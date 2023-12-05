#!/usr/bin/python3
'''Define this class Rectangle that inherits from Base Geometry'''
BaseGeometry = __import__('7-base geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represent a rectangle the inherit from Base Geometry'''

    def __init__(self, width, height):
        '''Initialise a new Rectangle

        Args:
           width (int): This width of the new Rectangle
           height (int): This height of the new Rectangle
        '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Return this area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Return this print() and str() representation of this Rectangle'''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)

        return string
