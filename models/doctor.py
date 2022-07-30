#!usr/bin/pyhton3
""" A class Doctor that inherits from Staff """
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.staff import Staff


class Doctor(Staff):
    """ Simple Doctor class model """
    __tablename__ = "doctors"

    staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                      primary_key=True)
    job_title = Column(String(16), nullable=False, default="Doctor")
    consultations = relationship("Consultation", backref="doctor")
    prescriptions = relationship("Prescription", backref="doctor")
    role = 'doctor'

    __mapper_args__ = {
        "polymorphic_identity": "doctor"
    }
