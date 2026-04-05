#!/usr/bin/python3
"""This module defines a class named 'Square' with a private instance
attribute 'size'"""


class Square:
    """Defines a square by its 'size' which is a private instance attribute"""
    def __init__(self, size):
        self.__size = size
