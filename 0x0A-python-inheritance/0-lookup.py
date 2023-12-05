#!/usr/bin/python3
'''Define an this object attribute lookup function'''


def lookup(obj):
    '''Return this list of available attribute and method of this object.'''
    return (dir(obj))
