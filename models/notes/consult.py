#!/usr/bin/python3
"""Module for Consultation class."""
from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Consultation(BaseModel, Base):
    """Class representing a Consultation"""
    __tablename__ = "consultations"

    created_by = Column(Integer,
                        ForeignKey("doctors.staff_id", ondelete='SET NULL'))
    pid = Column(Integer,
                 ForeignKey('patients.pid', ondelete='CASCADE'),
                 nullable=False)
    pc = Column(Text)
    hpc = Column(Text)
    pohx = Column(Text)
    pghx = Column(Text)
    pmhx = Column(Text)
    prov_diag = Column(Text, nullable=False)
    plan = Column(Text)
    doctor_name = Column(String(60))
    patient = relationship('Patient', back_populates='consultations')
    vitals = relationship('VitalSign', back_populates='consultation',
                          uselist=False)
    prescription = relationship('Prescription', cascade='all, delete',
                                 back_populates='consultation', uselist=False)

    def __init__(self, *args, **kwargs):
        """calls the super init and set doctor_name"""
        super().__init__(*args, **kwargs)
        if self.created_by is not None:
            from storage import storage
            doc = storage.get('Doctor', 'staff_id', self.created_by)
            self.doctor_name = f"Dr {doc.first_name} {doc.last_name}"
