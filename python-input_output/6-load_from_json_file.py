#!/usr/bin/python3
"""This module contains load_from_json_file() function"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Prameters
    ---------
        filename : str
    Return
    ------
        object
            Python object representation of the json file
    """
    with open(filename, "r", encoding="UTF-8") as file:
        obj = json.load(file)
    return obj
