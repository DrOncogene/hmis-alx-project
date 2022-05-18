#!/usr/bin/python3
"""Module for Permissions class
Contains the Permissions class for the HMIS console.
"""

import uuid
from datetime import datetime
from models import storage


class Permissions:

    """Class for permissions of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Permissions instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.created_by = ""
            self.updated_at = datetime.now()
            self.updated_by = ""
            items = []
            create = ""
            edit = ""
            delete = ""
            view = ""
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self, users_id):
        """Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()
        self.updated_by = users_id
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
