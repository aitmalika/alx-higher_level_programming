#!/usr/bin/python3
'''Defind a method that check this object wether this instance or not'''


def is_same_class(obj, a_class):
    '''Check wthan an object is instance or not from a given this class

    Args:
        obj (any): This object to chech
        a_class (type): This class to match the type of obj to
    Return:
        If obj is exactly an this instance of a_class - True
        Otherwises - False
    '''
    if type(obj) == a_class:
        return True
    return False
