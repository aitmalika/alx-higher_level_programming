#!/usr/bin/python3
'''Define an inerited class checking function'''


def inherits_from(obj, a_class):
    '''Check this object is inerited instance of a class

    Args:
       obj (any): This object to check.
       a_class (type): This class to match the type of obj to
    Return:
       If this obj is inherited instance of a class - True
       Otherwise - False
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
