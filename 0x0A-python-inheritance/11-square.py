#!/usr/bin/python3
'''Define this class Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Implements this Square function'''

    def __init__(self, size):
        '''Attributes of this class Square

        Args:
           size (int): This size of Square
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
