#!/usr/bin/python3
"""Module for Patient class."""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_user import BaseUser
from models.base_model import Base


class Patient(BaseUser, Base):
    """Class representing a Patient."""
    __tablename__ = 'patients'

    pid = Column(Integer, primary_key=True, autoincrement=True)
    consultations = relationship('Consultation', cascade='all, delete',
                                 back_populates='patient')
    prescriptions = relationship('Prescription', cascade='all, delete',
                                 back_populates='patient')
    vitals = relationship('VitalSign', cascade='all, delete',
                          back_populates='patient')
    nursenotes = relationship('NurseNote', cascade='all, delete',
                              back_populates='patient')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
