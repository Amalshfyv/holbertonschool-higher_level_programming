#!/usr/bin/python3
"""This module contains Studen calss"""


class Student:
    """
    This class defines a student

    Attributes
        str : first_name
        str : last_name
        age : int

    Methods
    -------
        to_json() -> dict
            Retrieves a dictionary representation of a Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__
