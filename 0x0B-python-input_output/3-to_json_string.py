#!/usr/bin/python3
"""Module containing this function to_json_string"""
import json


def to_json_string(my_obj):
    """Return this JSON representation of an object(string)

    Args:
        my_obj (type): this object to examin

    Return:
        str: JSON this representation of object
    """
    # print("type json.dumps(my_obj)--> {}".format(type(json.dumps(my_obj))))
    # print("type my_obj--> {}".format(type(my_obj)))

    # serialising json
    return json.dumps(my_obj)
