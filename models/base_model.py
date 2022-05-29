#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the HMIS console.
"""
from os import getenv as osgetenv
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
# storage is imported within necessary methods

Base = declarative_base()


class BaseModel:
    """Class for base model of object hierarchy."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.utcnow(),
                        nullable=False)
    created_by = Column('created_by', String(60))
    updated_at = Column(DateTime(timezone=True),
                        default=datetime.utcnow(),
                        onupdate=datetime.utcnow(), nullable=False)
    updated_by = Column(String(60))

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
            try:
                del kwargs['__class__']
            except KeyError:
                pass
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
        obj_dict = self.__dict__.copy()
        if osgetenv('STORAGE_TYPE') == 'db' and hasattr(self, 'staff_id'):
            titles = {
                "Admin": "ADM",
                "Doctor": "DOC",
                "Nurse": "NRS",
                "Pharmacist": "PHM",
                "RecordOfficer": "REC"
            }
            title = title = titles[self.__class__.__name__]
            obj_dict['staff_id'] = f'{title}{self.staff_id:04d}'
        del obj_dict['_sa_instance_state']
        return "[{}] {}".\
            format(type(self).__name__, obj_dict)

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
        try:
            del my_dict['_sa_instance_state']
        except KeyError:
            pass
        return my_dict
