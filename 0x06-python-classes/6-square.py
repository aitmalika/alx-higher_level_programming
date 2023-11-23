#!/usr/bin/python3
"""Square generations module for Python project 0x06
"""


class Square:
    """Class defined for square generations

    Args:
        size (int): length of one side of squared
        position (tuple) ((int), (int)): horizontal offset in space
        vertical offe set in new line


    Attributes:
        __size (int): length of one side of squared
        __position (tuple) ((int), (int)): horizontal offe set in space
        vertical offe set in new line


    """
    def __init__(self, size=0, position=(0, 0)):
        # attribute assigment here engages setter defined below
        self.size = size
        self.position = position

    @property
    def size(self):
        """__size getter, setter with same method names

        Returns:
            __size (int): length of one side, square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): length of one side this of square

        Attributes:
            __size (int): length of one side the of square

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
        """__position get ter, set ter with same method name

        Returns:
            __position (tuple) ((int), (int)): horizontal offe set in spaces
            vertical offe set in new line

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Args:
            value (int): tuple of two positives integer

        Attributes:
            __position (tuple) ((int), (int)): horizontal offe set in space
            vertical offe set in new line

        Raises:
            TypeError: if value is not a tuple of two positives int

        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integer')
        if len(value) is not 2:
            raise TypeError('positions must be a tuple of 2 positive integer')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('positions must be a tuple of ' +
                                '2 positive integer')
        self.__position = value

    def area(self):
        """Calulate area of square

        Attributes:
            __size (int): length of one side of squares

        Returns:
            area (int): length of one side, square

        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Print text representation of square in hash Char,
        horizontal and vertical offe set by first and second int
        in __position, respecti vely

        Attributes:
            __size (int): length of one side of square
            __position (tuple) ((int), (int)): horizontal offe set in spaces
            vertical offe set in new lin

        """
        if self.__size is 0:
            print()
        else:
            for v_offset in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for h_offset in range(0, self.__position[0]):
                    print(" ", end="")
                for col in range(0, self.__size):
                    print("#", end="")
                print()

#        print("size: {} position: {}".format(self.__size, self.__position))
