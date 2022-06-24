#!/usr/bin/python3
"""Module for Consultation class."""
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Consultation(BaseModel, Base):
    """Class representing a Consultation"""
    __tablename__ = "consultations"

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
    patient = relationship('Patient', back_populates='consultations')
    vitals = relationship('VitalSign', back_populates='consultation')
    prescriptions = relationship('Prescription', cascade='all, delete',
                                 back_populates='consultation')
