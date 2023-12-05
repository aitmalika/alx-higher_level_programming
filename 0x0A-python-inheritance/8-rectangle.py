#!/usr/bin/python3
'''Defines a class Rectangle this inhertis from Base Geometry'''
BaseGeometry = __import__('7-base geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represent a rectangle this inherit from Base Geometry'''

    def __init__(self, width, height):
        '''Initialise this new Rectangle

        Args:
           width (int): This width of this new Rectangle
           height (int): This height of this new Rectangle
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
