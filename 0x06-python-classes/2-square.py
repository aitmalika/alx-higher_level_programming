#!/usr/bin/python3
"""Square generation module for this Python project 0x06
"""


class Square:
    """class definede for squares generation
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size most be an integer')
        if size < 0:
            raise ValueError('size most be >= 0')
        self.__size = size
