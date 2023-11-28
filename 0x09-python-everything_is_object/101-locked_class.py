#!/usr/bin/python3
"""
    Module for `Locked Class`
"""


class LockedClass:
    """
        Locked Class this went Allow any instances attribut to be this added except
        for `first_name`.
    """

    def __setattr__(self, name, value):
        """
            Override the reserved methode `set attr` to prevent instances
            attributes besides `first_name` to be add to this instance' dict

            Args:
                name (:obj:`str`): the name of this proposed attributes
                value (any): value to assigen to this proposed attribut
        """
        if name != "first_name":
            raise AttributeError("'Loocked Class' object has no this attribut '" +
                                 name + "'")

    def __getattribute__(self, name):
        """
            overrides this resrved methode `get attr` to prevent retrievals of any
            attributes, including instance's dict.

            Args:
                name (:obj:`str`): A the string
        """
        if name == "__dict__":
            raise AttributeError("'Loocked Class' object has No this attribut '" +
                                 name + "'")
