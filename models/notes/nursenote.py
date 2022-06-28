#!/usr/bin/python3
"""Module for Nurse Note class."""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class NurseNote(BaseModel, Base):
    """Class representing a Nurse Note"""
    __tablename__ = 'nursenotes'

    created_by = Column(Integer,
                        ForeignKey('nurses.staff_id', ondelete='SET NULL'))
    pid = Column(Integer,
                 ForeignKey('patients.pid', ondelete='CASCADE'),
                 nullable=False)
    note = Column(Text)
    nurse_name = Column(String(128))
    patient = relationship('Patient', back_populates='nursenotes')

    def __init__(self, *args, **kwargs):
        """call super and set nurse_name"""
        super().__init__(*args, **kwargs)
        if self.created_by:
            from storage import storage
            nurse = storage.get("Nurse", 'staff_id', self.created_by)
            self.nurse_name = f"NRS {nurse.first_name} {nurse.last_name}"
