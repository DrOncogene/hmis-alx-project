#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json


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
            json.dump(json_objects, f, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = import_models()
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except Exception:
            pass

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
        """returns a single obj of cls with id"""
        key = "{}.{}".format(cls.__name__, id)
        return self.__objects[key] if key in self.__objects else None

    def count(self, cls=None):
        """ count the number of objs in storage of cls, if given"""
        return len(self.all(cls))


def import_models():
    from models.patient import Patient
    from models.doctor import Doctor
    from models.nurse import Nurse
    from models.pharmacist import Pharmacist
    from models.record import RecordOfficer
    from models.admin import Admin
    from models.notes.consult import Consultation
    from models.notes.prescription import Prescription
    from models.notes.vitals import VitalSign
    from models.notes.nursenote import NurseNote
    from models.drug import Drug

    return {
        "Patient": Patient,
        "Doctor": Doctor,
        "Nurse": Nurse,
        "Pharmacist": Pharmacist,
        "RecordOfficer": RecordOfficer,
        "Admin": Admin,
        "Consultation": Consultation,
        "Prescription": Prescription,
        "VitalSign": VitalSign,
        "NursesNote": NurseNote,
        "Drug": Drug
    }
