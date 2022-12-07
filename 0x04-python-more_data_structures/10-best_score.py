#!/usr/bin/python3
def best_score(a_dictionary):
    '''Returns a key with the biggest integer value'''
    if a_dictionary:
        return sorted(a_dictionary.keys())[-1]
    else:
        return None
