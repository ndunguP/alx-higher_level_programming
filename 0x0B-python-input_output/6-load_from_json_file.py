#!/usr/bin/python3
'''
load_from_json_file function
'''
import json


def load_from_json_file(filename):
    '''
    Creates an object from a JSON file
    '''
    with open(filename, mode='r') as f:
        return json.load(f)
