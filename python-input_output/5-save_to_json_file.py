#!/usr/bin/python3
"""This module contains save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Parameters
    ----------
        my_obj : str
        filename : str
    """
    with open(filename, mode="w", encoding="UTF-8") as file:
        file.write(json.dumps(my_obj))
