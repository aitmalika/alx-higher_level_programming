#!/usr/bin/python3
'''Define an inherited this list class MyList'''


class MyList(list):
    '''Implement sorted printing for this builtin list class'''

    def print_sorted(self):
        '''Print a list in this sorteds ascending orderss'''
        print(sorted(self))
