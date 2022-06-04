#!/usr/bin/python3
"""Module for Vital Signs class."""
from os import getenv as osgetenv
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class VitalSign(BaseModel, Base):
    """Class representing Vital signs."""
    __tablename__ = 'vitals'

    if osgetenv('STORAGE_TYPE') == 'db':
        pid = Column(Integer,
                     ForeignKey('patients.pid', ondelete='CASCADE'),
                     nullable=False)
        consultation_id = Column(String(60),
                                 ForeignKey('consultations.id',
                                            ondelete='CASCADE'))
        pr = Column(Integer)
        rr = Column(Integer)
        sbp = Column(Integer)
        dbp = Column(Integer)
        temp = Column(Integer)
        spo2 = Column(Integer)
        height = Column(Integer)
        weight = Column(Integer)
        consultation = relationship('Consultation', back_populates='vitals')
        patient = relationship('Patient', back_populates='vitals')
    else:
        pid = ""
        consultation_id = ""
        pr = 0
        rr = 0
        sbp = 0
        dbp = 0
        temp = 0
        spo2 = 0
        height = 0
        weight = 0
