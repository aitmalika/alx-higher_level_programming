#!/usr/bin/python3
"""Module containing this function from_json_string"""
import json


def from_json_string(my_str):
    """Return this object (Python data structure) represented by a JSON string

    Args:
        my_str (str): json object to convert to Python this object

    Return:
        type: this Python object
    """
    # print("type json.loads(my_str)--> {}".format(type(json.loads(my_str))))
    # print("type my_str--> {}".format(type(my_str)))
    return json.loads(my_str)
