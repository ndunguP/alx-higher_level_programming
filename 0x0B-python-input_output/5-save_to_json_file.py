#!/usr/bin/python3
'''
save_to_json_file
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an object to a text file using JSON representation
    '''
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
