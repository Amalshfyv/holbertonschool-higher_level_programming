#!/usr/bin/python3
"""Expands BaseGeometry class to include integer validation"""


class BaseGeometry:
    """BaseGeometry class with methods to raise an exception for
    unimplemented area and validate integer values"""

    def area(self):
        """Raises an Exception with the message that the method is
        not implemented.

        Raises:
            Exception: "area() is not implemented" """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
