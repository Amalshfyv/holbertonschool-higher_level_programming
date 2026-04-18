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
        reload_from_json()
            replaces all attributes of the Student instance
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        set1 = set(self.__dict__.keys())
        set2 = set(attrs)
        d = {key: self.__dict__[key] for key in list(set1.intersection(set2))}
        return d

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if not len(json) is 0:
            self.__dict__ = json
