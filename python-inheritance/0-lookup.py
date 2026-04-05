#!/usr/bin/python3
"""Module that defines the lookup function."""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be returned.

    Returns:
        list: A list of strings representing the attributes and methods
        of the object.
    """
    return dir(obj)
