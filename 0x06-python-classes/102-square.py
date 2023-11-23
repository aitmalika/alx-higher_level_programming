#!/usr/bin/python3
"""Squares generation module for this Python project 0x06
"""


class Square:
    """Class defined for squared generations

    Args:
        size (int): length of one side of squared

    Attributes:
        __size (int): length of one side of squared

    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """__size getter, set ter with same method names

        Returns:
            __size (int): length of one side, square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): length of one side of squared

        Attributes:
            __size (int): length of one side of squared

        Raises:
            TypeError: if value is not an integere
            ValueError: if value is less than 0

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calulate area of square

        Attributes:
            __size (int): length of one side of squared

        Returns:
            area (int): length of one side, square

        """
        area = self.__size * self.__size
        return area

    def __lt__(self, other):
        """Define comparison of class object for less than
        Taken from Comparison
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Define comparison of class object for less than equal to
        taken from Comparison
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Define comparison of class object for equal to
        Taken from Comparison
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Define comparison of class object for not equal to
        Taken from Comparison
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Define comparison of class object for greate than
        Taken from Comparison
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Define comparison of class object for greate than equal to
        Taken Comparison
        """
        return self.area() >= other.area()
