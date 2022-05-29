#!usr/bin/pyhton3
""" A class Nurse that inherits from Staff """
from os import getenv as osgetenv
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base
from models.staff import Staff
from models.permissions import Permission


class Nurse(Staff, Base):
    """ Simple Nurse class model """
    __tablename__ = "nurses"

    if osgetenv('STORAGE_TYPE') == 'db':
        job_title = Column(String(16), nullable=False, default="Nurse")
        permissions = Column(String(60), ForeignKey('permissions.id'))
    else:
        job_title = "Nurse"
        permissions = Permission(
            create=('vitals', 'nursenote'),
            edit=('vitals', 'nursenote'),
            delete=('vitals', 'nursenote'),
            view=('all')
        )

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            if osgetenv('STORAGE_TYPE') != 'db':
                super().set_staff_id()
