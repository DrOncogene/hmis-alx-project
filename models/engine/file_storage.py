#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from os import path as os_path


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        models = import_models()
        if os_path.exists(FileStorage.__file_path):
            with open(f"{FileStorage.__file_path}", "r") as f:
                json_str = f.read()
                if len(json_str) == 0:
                    return
                loaded_dict = json.loads(json_str)
                FileStorage.__objects.clear()
                for key, obj_dict in loaded_dict.items():
                    obj_class = models[key.split(".")[0]]
                    FileStorage.__objects[key] = obj_class(**obj_dict)

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

def import_models():
    """imports the modules locally when called
    to avoid circular import"""
    from models.base_model import BaseModel
    from models.consult import Consult
    from models.drug import Drug
    from models.patient import Patient
    from models.prescription import Prescription
    from models.staff import Staff
    from models.vitals import Vitals


    models = {"BaseModel": BaseModel, "Consult": Consult, "Drug": Drug,
        "Patient": Patient, "Prescription": Prescription,
        "Vitals": Vitals, "Staff": Staff}

    return models