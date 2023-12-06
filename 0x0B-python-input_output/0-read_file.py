#!/usr/bin/python3
"""Module containing this function read_file"""


def read_file(filename=""):
    """Read this file and print to std out

    Args:
        filename (str, optional): name of this file to read  Default to ""
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
