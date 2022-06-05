#!usr/bin/pyhton3
""" A class Doctor that inherits from Staff """
from sqlalchemy import Column, String, Integer, ForeignKey
from models.staff import Staff
from models.permissions import Permission


class Doctor(Staff):
    """ Simple Doctor class model """
    __tablename__ = "doctors"

    staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                      primary_key=True)
    job_title = Column(String(16), nullable=False, default="Doctor")
    permissions = Column(String(60), ForeignKey('permissions.id'))

    __mapper_args__ = {
        "polymorphic_identity": "doctor"
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
