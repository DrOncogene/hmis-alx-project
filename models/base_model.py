#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the HMIS console.
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_mixin, declared_attr
from sqlalchemy.sql import func
# storage is imported within necessary methods

Base = declarative_base()


@declarative_mixin
class BaseModel:
    """Class for base model of object hierarchy."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, default=func.now(),
                        onupdate=func.now(), nullable=False)

    @declared_attr
    def created_by(cls):
        return Column(Integer, ForeignKey('staffs.staff_id'))

    @declared_attr
    def updated_by(cls):
        return Column(Integer, ForeignKey('staffs.staff_id'))

    def __init__(self, *args, **kwargs):
        """Initialization of a BaseModel instance"""
        if 'created_at' not in kwargs:
            from storage import storage
            self.id = str(uuid.uuid4())
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            try:
                del kwargs['__class__']
            except KeyError:
                pass
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""
        obj_dict = self.__dict__.copy()
        if hasattr(self, 'staff_id'):
            obj_dict['staff_id'] = self.format_staff_id()
        del obj_dict['_sa_instance_state']
        return "[{}] {}".\
            format(type(self).__name__, obj_dict)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""
        from storage import storage
        self.updated_at = datetime.now()
        self.updated_by = None
        storage.save()

    def delete(self):
        """Deletes an object and updates the updated_at attribute
        with the current datetime."""
        from storage import storage
        storage.delete(self)

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        if hasattr(self, 'staff_id'):
            my_dict['staff_id'] = self.format_staff_id()
        try:
            del my_dict['_sa_instance_state']
        except KeyError:
            pass
        return my_dict
