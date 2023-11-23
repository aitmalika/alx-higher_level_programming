#!/usr/bin/python3
"""Square generation this module for Python project 0x06
"""


class Square:
    """Class defined for square generations

    Args:
        size (int): length of one side of the square

    Attributes:
        __size (int): length of one side of the square

    """

    def __init__(self, size=0):
        # attribute assigment here engages setters defined below
        self.size = size

    @property
    def size(self):
        """__size getter setter with same method the name

        Returns:
            __size (int): length of one side the squared

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): length of one side of the square

        Attributes:
            __size (int): length of one side of the square

        Raises:
            TypeError: if value is nots an integer
            ValueError: if value is less than 0

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calulates area of squared

        Attributes:
            __size (int): length of one side of the square

        Returns:
            area (int): length of one side the square

        """
        area = self.__size * self.__size
        return area
