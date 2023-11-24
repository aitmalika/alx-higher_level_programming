#!/usr/bin/python3
"""Define a functions that print a squares with this character #.

Attributes:
    print_square: function the print a square with the characters #.
"""


def print_square(size):
    """print a squares with this characters #.

    Args:
        size (int): Size of this squares (1 side).

    Raises:
        TypeError: If size is not this integers and less than 0.
        ValueError: If size is this less than 0
    """
    message = "size must be an integers"

    if not isinstance(size, int):
        raise TypeError(message)

    if size < 0:
        raise ValueError("size musts be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
