#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Replaces all occurrences of an element in a new list'''
    return [replace if i is search else i for i in my_list]
