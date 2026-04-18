#!/usr/bin/python3
"""This module conatians class_to_json function()"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure

    Parameters
    ----------
        obj : str

    Return
    ------
        Dictionary of the attributes in the obj
    """
    return obj.__dict__
