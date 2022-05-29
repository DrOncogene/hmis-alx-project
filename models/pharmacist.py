#!usr/bin/pyhton3
""" A class Pharmacist that inherits from Staff """
from os import getenv as osgetenv
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base
from models.staff import Staff
from models.permissions import Permission


class Pharmacist(Staff, Base):
    """ Simple Pharmacist class model """
    __tablename__ = "pharmacists"

    if osgetenv('STORAGE_TYPE') == 'db':
        job_title = Column(String(16), nullable=False, default="Pharmacist")
        permissions = Column(String(60), ForeignKey('permissions.id'))
    else:
        job_title = "Pharmacist"
        permissions = Permission(
            create=('Drug'),
            edit=('prescription', 'Drug'),
            delete=('Drug'),
            view=('prescription', 'Drug')
        )

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            if osgetenv('STORAGE_TYPE') != 'db':
                super().set_staff_id()
