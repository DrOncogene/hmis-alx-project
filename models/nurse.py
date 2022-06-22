#!usr/bin/pyhton3
""" A class Nurse that inherits from Staff """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.staff import Staff


class Nurse(Staff):
    """ Simple Nurse class model """
    __tablename__ = "nurses"

    staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                      primary_key=True)
    job_title = Column(String(16), nullable=False, default="Nurse")
    permissions = Column(String(60), ForeignKey('permissions.id'))

    __mapper_args__ = {
        "polymorphic_identity": "nurse"
    }

    def __init__(self, **kwargs):
        """call the super"""
        super().__init__(**kwargs)
