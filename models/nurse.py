#!usr/bin/pyhton3
""" A class Nurse that inherits from Staff """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.staff import Staff


class Nurse(Staff):
    """ Simple Nurse class model """
    __tablename__ = "nurses"

    staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                      primary_key=True)
    job_title = Column(String(16), nullable=False, default="Nurse")
    nursenotes = relationship("NurseNote", backref="nurse")
    vitals = relationship("VitalSign", backref="nurse")
    role = 'nurse'

    __mapper_args__ = {
        "polymorphic_identity": "nurse"
    }
