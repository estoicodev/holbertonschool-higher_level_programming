#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The example module supplies one function, text_indentation().
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    start = 0
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[start:i + 1], end="\n\n")
            start = i + 1
            while text[start] == " ":
                start += 1
        if i == len(text) - 1:
            print(text[start:], end="")
