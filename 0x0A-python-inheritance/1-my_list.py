#!/usr/bin/python3
"""Module for my list """


class MyList(list):
    """Subclass MyList that inherits from list"""

    def print_sorted(self):
        """Print sorted list"""

        print(sorted(self))
