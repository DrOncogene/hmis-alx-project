#!/usr/bin/python3
"""Module for Vital Signs class."""
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class VitalSign(BaseModel, Base):
    """Class representing Vital signs."""
    __tablename__ = 'vitals'

    created_by = Column(Integer,
                        ForeignKey('nurses.staff_id', ondelete='SET NULL'))
    pid = Column(Integer,
                 ForeignKey('patients.pid', ondelete='CASCADE'),
                 nullable=False)
    consultation_id = Column(String(60),
                             ForeignKey('consultations.id',
                                        ondelete='CASCADE'),
                             unique=True)
    pr = Column(Integer)
    rr = Column(Integer)
    sbp = Column(Integer)
    dbp = Column(Integer)
    temp = Column(Float(precision=1))
    spo2 = Column(Integer)
    height = Column(Float(precision=1))
    weight = Column(Float(precision=1))
    nurse_name = Column(String(128))
    consultation = relationship('Consultation', back_populates='vitals')
    patient = relationship('Patient', back_populates='vitals')

    def __init__(self, *args, **kwargs):
        """call super and set nurse_name"""
        super().__init__(*args, **kwargs)
        if self.created_by is not None:
            from storage import storage
            nurse = storage.get("Nurse", 'staff_id', self.created_by)
            self.nurse_name = f"Nrs {nurse.get_full_name()}"
