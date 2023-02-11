#!/usr/bin/python3
'''
class Base
'''
import json


class Base:
    ''' Base class with initialization '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries '''
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objst to a file '''
        try:
            json_string = cls.to_json_string(
                [x.to_dictionary() for x in list_objs])
        except BaseException:
            json_string = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string rep of json_string '''
        return json.loads(json_string or '[]')

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attr set '''
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        if cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                dict_list = cls.from_json_string(f.read())
            return ([cls.create(**x) for x in dict_list])
        except FileNotFoundError:
            return []
