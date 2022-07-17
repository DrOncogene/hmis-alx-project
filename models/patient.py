#!/usr/bin/python3
"""Module for Patient class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_user import BaseUser
from models.base_model import Base


class Patient(BaseUser, Base):
    """Class representing a Patient."""
    __tablename__ = 'patients'

    created_by = Column(Integer,
                        ForeignKey('record_officers.staff_id',
                                   ondelete='SET NULL'))
    pid = Column(Integer, primary_key=True, autoincrement=True)
    record_officer = Column(String(60))
    consultations = relationship('Consultation', cascade='all, delete',
                                 back_populates='patient')
    prescriptions = relationship('Prescription', cascade='all, delete',
                                 back_populates='patient')
    vitals = relationship('VitalSign', cascade='all, delete',
                          back_populates='patient')
    nursenotes = relationship('NurseNote', cascade='all, delete',
                              back_populates='patient')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.created_by is not None:
            from storage import storage
            record = storage.get("RecordOfficer", 'staff_id', self.created_by)
            self.record_officer = f"{record.first_name} {record.last_name}"
