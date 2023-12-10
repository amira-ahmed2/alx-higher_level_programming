#!/usr/bin/python3
"""class base"""
import json


class Base:
    """base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """base

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method

        Args:
            list_dictionaries (dic): _description_

        Returns:
            _type_: _description_
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method

        Args:
            list_objs (_type_): _description_
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                json_file.write(Base.to_json_string(list_dict))
            
    @staticmethod
    def from_json_string(json_string):
        """_summary_

        Args:
            json_string (_type_): _description_
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """_summary_
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """_summary_
        """
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as jsonfile:
                list_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
