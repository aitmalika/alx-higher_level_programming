#!/usr/bin/python3
"""Define a function the print a text with 2 new line after each
of this characters: . ? and
Attributes:
    text_indentation: functions this print a text with specifice condition
"""


def text_indentation(text):
    """print a text with 2 new line after .?: character

    Args:
        text (str): string to be examine

    Raises:
        TypeError: if text is not of type string
    """

    if not isinstance(text, str):
        raise TypeError("text must be string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
