#!/usr/bin/python3

"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review



class FileStorage:
    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass  # No need to raise an error if the file doesn't exist

