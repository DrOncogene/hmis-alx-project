#!usr/bin/pyhton3
""" A class Admin that inherits from Staff """
from os import getenv as osgetenv
from sqlalchemy import Column, Integer, String, ForeignKey
from models.staff import Staff
from models.permissions import Permission


class Admin(Staff):
    """ Simple Admin class model """
    __tablename__ = "admins"

    if osgetenv('STORAGE_TYPE') == 'db':
        staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                          primary_key=True)
        job_title = Column(String(16), nullable=False, default="Admin")
        permissions = Column(String(60), ForeignKey('permissions.id'))
    else:
        job_title = "Admin"

    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            if osgetenv('STORAGE_TYPE') != 'db':
                super().set_staff_id()
