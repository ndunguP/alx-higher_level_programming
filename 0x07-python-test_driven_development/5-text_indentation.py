#!/usr/bin/python3
"""Module for text_indentation"""


def text_indentation(text):
    """text_indentation - indent and print text according to cases

    Args:
    text - text to indent and print
    """
    flag = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    textcpy = text.strip(" ")
    for i in textcpy:
        if i == '.' or i == '?' or i == ':':
            print("{}\n\n".format(i), end="")
            flag = 1
        elif i == " " and flag == 1:
                pass
        else:
            print("{}".format(i), end="")
            if i == '\n':
                flag = 1
            else:
                flag = 0
