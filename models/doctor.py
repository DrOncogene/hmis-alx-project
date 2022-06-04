#!usr/bin/pyhton3
""" A class Doctor that inherits from Staff """
from os import getenv as osgetenv
from sqlalchemy import Column, String, Integer, ForeignKey
from models.staff import Staff
from models.permissions import Permission


class Doctor(Staff):
    """ Simple Doctor class model """
    __tablename__ = "doctors"

    if osgetenv('STORAGE_TYPE') == 'db':
        staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                          primary_key=True)
        job_title = Column(String(16), nullable=False, default="Doctor")
        permissions = Column(String(60), ForeignKey('permissions.id'))
    else:
        job_title = "Doctor"
        permissions = Permission(
            create=('consultation', 'prescription'),
            edit=('consultation', 'prescription'),
            delete=('consultation', 'prescription'),
            view=('all')
        )

    __mapper_args__ = {
        "polymorphic_identity": "doctor"
    }

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            # if it's a new instantiation, generate a staff_id
            super().__init__()
            if osgetenv('STORAGE_TYPE') != 'db':
                super().set_staff_id()
