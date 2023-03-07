#!usr/bin/pyhton3
""" A class Records that inherits from Staff """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.staff import Staff


class RecordOfficer(Staff):
    """ Simple RecordOfficer class model """
    __tablename__ = "record_officers"

    staff_id = Column(Integer, ForeignKey("staffs.staff_id"),
                      primary_key=True)
    job_title = Column(String(16), nullable=False, default="RecordOfficer")
    role = 'recordofficer'

    __mapper_args__ = {
        "polymorphic_identity": "recordofficer"
    }
