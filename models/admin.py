#!usr/bin/pyhton3
""" A class Admin that inherits from Staff """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.staff import Staff


class Admin(Staff):
    """ Simple Admin class model """
    __tablename__ = "admins"

    staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                      primary_key=True)
    job_title = Column(String(16), nullable=False, default="Admin")
    permissions = Column(String(60), ForeignKey('permissions.id'))

    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
