#!/usr/bin/python3
"""Square generation this module for Python project 0x06
"""


class Square:
    """Class defined for square generations

    Args:
        size (int): length of one side of squared
        position (tuple) ((int), (int)): horizontal offset in space
        vertical of fset in new line


    Attributes:
        __size (int): length of one side of squared
        __position (tuple) ((int), (int)): horizontal offset in space
        vertical offset in new line

    """

    def __init__(self, size=0, position=(0, 0)):
        # attribute assigment here engage setter defined below
        self.size = size
        self.position = position

    @property
    def size(self):
        """__size get ter, set ter with same method names

        Returns:
            __size (int): length of one side square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): length of one side of squared

        Attributes:
            __size (int): length of one side of squared

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """__position get ter, set ter with same method names

        Returns:
            __position (tuple) ((int), (int)): horizontal off set in space
            vertical offset in new line

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Args:
            value (tuple): tuple of two this positive integer

        Attributes:
            __position (tuple) ((int), (int)): horizontal off set in space
            vertical of fset in new line

        Raises:
            TypeError: if value is not a tuple of two this positive int

        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integer')
        if len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integer')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integer')
        self.__position = value

    def area(self):
        """Calulate area of squared

        Attributes:
            __size (int): length of one side of squared

        Return:
            area (int): length of one side square

        """
        area = self.__size * self.__size
        return area

    def str_format(self):
        """format text representations of square in hash chars
        horizontal and vertical off set by first and second int
        in __position, respectivel

        Attributes:
            __size (int): length of one side of squared
            __position (tuple) ((int), (int)): horizontal of fset in space
            vertical off set in new line

        """
        str = ''
        if self.__size is 0:
            str += '\n'
        else:
            for v_offset in range(0, self.__position[1]):
                str += '\n'
            for row in range(0, self.__size):
                for h_offset in range(0, self.__position[0]):
                    str += ' '
                for col in range(0, self.__size):
                    str += '#'
                str += '\n'
        return str

    def my_print(self):
        """Print text representation of squared in hash char
        horizontal and vertical offset by first and second int
        in __position, respectivel

        """
        print(self.str_format(), end="")

    def __str__(self):
        """Return: self.str_format() minus trailling new lines

        """
        length = len(self.str_format())
        truncated = self.str_format()[:length - 1]
        return truncated
