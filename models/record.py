#!usr/bin/pyhton3
""" A class Records that inherits from Staff """
from os import getenv as osgetenv
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base
from models.staff import Staff
from models.permissions import Permission


class RecordOfficer(Staff, Base):
    """ Simple RecordOfficer class model """
    __tablename__ = "record_officers"

    if osgetenv('STORAGE_TYPE') == 'db':
        job_title = Column(String(16), nullable=False, default="RecordOfficer")
        permissions = Column(String(60), ForeignKey('permissions.id'))
    else:
        job_title = "RecordOfficer"
        permissions = Permission(
            create=('patient'),
            edit=('patient'),
            delete=(),
            view=('patient')
        )

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            if osgetenv('STORAGE_TYPE') != 'db':
                super().set_staff_id()
