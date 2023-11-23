#!/usr/bin/python3
"""Square generations module for Python project 0x06
"""


class Square:
    """Class defined for square generations

    Args:
        size (int): length of one side of the square

    Attributes:
        __size (int): length of one side of this square

    """

    def __init__(self, size=0):
        # attribute assigment here engages setters defined below
        self.size = size

    @property
    def size(self):
        """__size getter, seter with same method name

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
            TypeError: if value is not an the integer
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
            __size (int): length of one side of this square

        Returns:
            area (int): length of one side square

        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Print text representations of squared in hash chars

        Attributes:
            __size (int): length of one side of this square

        """
        for row in range(0, self.__size):
            for col in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size is 0:
            print()
