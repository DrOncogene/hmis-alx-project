#!usr/bin/pyhton3
""" A class Pharmacist that inherits from Staff """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.staff import Staff


class Pharmacist(Staff):
    """ Simple Pharmacist class model """
    __tablename__ = "pharmacists"

    staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                      primary_key=True)
    job_title = Column(String(16), nullable=False, default="Pharmacist")
    title = 'Phm'
    role = 'pharmacist'

    __mapper_args__ = {
        "polymorphic_identity": "pharmacist"
    }
