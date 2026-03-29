#!/usr/bin/python3

"""This module contains a function for text indentation."""


def text_indentation(text):
    """
    Prints text with two new lines after each of the following: `. ? :`

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    length = len(text)
    i = 0
    while i < length:
        print(text[i], end="")
        if text[i] in ('.', '?', ':'):
            print(end="\n\n")
            while i + 1 < length and text[i + 1] == ' ':
                i += 1
        i += 1
