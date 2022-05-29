#!usr/bin/pyhton3
""" A class Admin that inherits from Staff """
from os import getenv as osgetenv
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base
from models.staff import Staff
from models.permissions import Permission


class Admin(Staff, Base):
    """ Simple Admin class model """
    __tablename__ = "admins"

    if osgetenv('STORAGE_TYPE') == 'db':
        job_title = Column(String(16), nullable=False, default="Admin")
        permissions = Column(String(60), ForeignKey('permissions.id'))
    else:
        job_title = "Admin"

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            if osgetenv('STORAGE_TYPE') != 'db':
                super().set_staff_id()
