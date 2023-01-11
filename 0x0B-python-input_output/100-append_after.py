#!/usr/bin/python3
'''
append_after function
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Inserts a line of text to a file, after each line containing
    a specific string
    '''
    with open(filename, mode='r', encoding='utf-8') as f:
        string = ""
        for line in f:
            if search_string in line:
                string += line + new_string
            else:
                string += line

    with open(filename, mode='w') as f:
        f.write(string)
