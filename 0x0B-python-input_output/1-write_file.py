#!/usr/bin/python3
'''
write_file function
'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file (UTF8) and returns the number
    of characters written
    '''
    with open(filename, mode='w', encoding='utf-8') as f:
        new_file = f.write(text)

    return new_file
