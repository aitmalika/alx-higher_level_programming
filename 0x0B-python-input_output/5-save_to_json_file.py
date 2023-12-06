#!/usr/bin/python3
"""Module containing this function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Write this Object to a text file using JSON representation

    Args:
        my_obj (type): Object to this write to text file
        file name (str): name of this file

    Return:
        type: the JSON representation
    """

    # print("type of json_object --> {}".format(type(json_object)))
    # print("type of my_obj --> {}".format(type(my_obj)))
    # print("type file name --> {}".format(type(filename)))
    # writing to file
    with open(filename, 'w', encoding="utf-8") as f:
        # serializing json
        json_object = json.dumps(my_obj)
        # or json.dump(my_obj, f)
        f.write(json_object)
        f.close()
