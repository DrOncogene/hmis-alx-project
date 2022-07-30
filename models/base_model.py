#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the HMIS console.
"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_mixin, declared_attr
from sqlalchemy.sql import func
# storage is imported within necessary methods

Base = declarative_base()


@declarative_mixin
class BaseModel:
    """Class for base model of object hierarchy."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        server_default=func.now())
    updated_at = Column(DateTime(timezone=True),  nullable=False,
                        server_default=func.now(), onupdate=func.now())

    @declared_attr
    def created_by(cls):
        return Column(Integer,
                      ForeignKey('staffs.staff_id', ondelete='SET NULL'))

    @declared_attr
    def updated_by(cls):
        return Column(Integer,
                      ForeignKey('staffs.staff_id', ondelete='SET NULL'))

    def __init__(self, *args, **kwargs):
        """Initialization of a BaseModel instance"""
        from storage import storage
        self.id = str(uuid.uuid4())
        storage.new(self)
        try:
            del kwargs['__class__']
        except KeyError:
            pass

        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""
        from storage import storage
        obj_dict = {}
        updated_obj = storage.get(type(self), 'id', self.id)
        obj_dict.update(updated_obj.__dict__)
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        if hasattr(self, 'staff_id'):
            obj_dict['staff_id'] = self.format_staff_id()
        obj_dict.pop('_sa_instance_state', None)
        obj_dict.pop('password', None)
        return "[{}] {}".\
            format(type(self).__name__, obj_dict)

    def save(self):
        """saves the obj to db"""
        from storage import storage
        storage.save()

    def delete(self):
        """Deletes an object and updates the updated_at attribute
        with the current datetime."""
        from storage import storage
        storage.delete(self)

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        from storage import storage
        obj_dict = {}
        updated_obj = storage.get(type(self), 'id', self.id)
        obj_dict.update(updated_obj.__dict__)
        if hasattr(self, 'staff_id'):
            obj_dict['staff_id'] = self.format_staff_id()
        obj_dict.pop('_sa_instance_state', None)
        obj_dict.pop('password', None)
        return obj_dict
