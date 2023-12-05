#!/usr/bin/python3
'''Define a this class and inherited clas chking function.'''


def is_kind_of_class(obj, a_class):
    '''Check this object is instance or inherited instance of a class

    Args:
       obj (any): This object to be checked
       a_class (type): This class to match the type of obj to
    Return:
       If obj is an instance or instance of a class True
       Otherwise False
    '''
    if isinstance(obj, a_class):
        return True
    return False
