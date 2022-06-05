#!/usr/bin/python3
"""Module for Nurse Note class."""
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class NurseNote(BaseModel, Base):
    """Class representing a Nurse Note"""
    __tablename__ = 'nursenotes'

    pid = Column(Integer,
                 ForeignKey('patients.pid', ondelete='CASCADE'),
                 nullable=False)
    note = Column(Text)
    patient = relationship('Patient', back_populates='nursenotes')
