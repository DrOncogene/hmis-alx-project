#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the HMIS console.
"""
import uuid
from datetime import datetime
# storage is import within necessary methods


class BaseModel:
    """Class for base model of object hierarchy."""
    def __init__(self, *args, **kwargs):
        """Initialization of a BaseModel instance"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            from storage import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.created_by = ""
            self.updated_at = self.created_at
            self.updated_by = ""
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""
        from storage import storage
        self.updated_at = datetime.now()
        self.updated_by = ""
        storage.save()

    def delete(self):
        """Deletes an object and updates the updated_at attribute
        with the current datetime."""
        from storage import storage
        storage.delete(self)

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
