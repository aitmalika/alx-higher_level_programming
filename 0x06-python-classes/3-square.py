#!/usr/bin/python3
"""Square generations module for Python project 0x06
"""


class Square:
    """Class defined for square generations

    Args:
        size (int): Length of one side of square

    Attributes:
        __size (int): length of one side of square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is les than 0

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size muste be an integer')
        if size < 0:
            raise ValueError('size muste be >= 0')
        self.__size = size

    def area(self):
        """Calulate area of square

        Attribute:
            __size (int): length of one side of square

        Returns:
            area (int): length of one side, squared

        """
        area = self.__size * self.__size
        return area
