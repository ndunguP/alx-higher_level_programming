#!/usr/bin/python3
"""Module to add new attribute to an object if possible"""


def add_attribute(self, name, value):
    """Add attrubute to object if possible
    Args:
    name: name of attribute
    value: value of attribute
    """
    if hasattr(self, "__dict__"):
        setattr(self, name, value)
    else:
        raise TypeError("can't add new attribute")
