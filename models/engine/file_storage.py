#!/usr/bin/python3
""" Module file_storage for the AirBnB console """
import json


class FileStorage:
    """ class that store information of the BaseModel Class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ method that returns all objects """
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            d = {i: j.to_dict() for i,
                 j in FileStorage.__objects.items()}
            json.dump(d, fp)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
                FileStorage.__objects = {i: BaseModel(**j) for i,
                                         j in data.items()}
        except Exception:
            pass
