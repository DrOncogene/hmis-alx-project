#!/usr/bin/python3
"""Module for Consultation class."""
from os import getenv as osgetenv
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Consultation(BaseModel, Base):
    """Class representing a Consultation"""
    __tablename__ = "consultations"

    if osgetenv('STORAGE_TYPE') == 'db':
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
    else:
        pid = ""
        prescription_ids = []
        vitals_ids = []
        pc = ""
        hpc = ""
        pohx = ""
        pghx = ""
        pmhx = ""
        prov_diag = ""
        plan = ""
