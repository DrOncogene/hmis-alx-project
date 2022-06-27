#!/usr/bin/python3
"""Module for Prescription class."""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Prescription(BaseModel, Base):
    """Class representing a Prescription."""
    __tablename__ = 'prescriptions'

    created_by = Column(Integer,
                        ForeignKey('doctors.staff_id', ondelete='SET NULL'))
    pid = Column(Integer,
                 ForeignKey('patients.pid', ondelete='CASCADE'),
                 nullable=False)
    consultation_id = Column(String(60),
                             ForeignKey('consultations.id',
                                        ondelete='CASCADE'),
                             nullable=False)
    dispensed_by = Column(Integer, ForeignKey('pharmacists.staff_id'))
    prescriber = Column(String(128))
    patient = relationship('Patient', back_populates='prescriptions')
    consultation = relationship('Consultation', back_populates='prescriptions')
    drugs = relationship('DrugPrescription', cascade='all, delete',
                         back_populates='prescription')

    def __init__(self, *args, **kwargs):
        """calls the super and set prescriber"""
        super().__init__(*args, **kwargs)
        if self.created_by:
            from storage import storage
            creator = storage.get('Doctor', 'staff_id', self.created_by)
            self.prescriber = f"{creator.first_name} {creator.last_name}"


class DrugPrescription(BaseModel, Base):
    """class representing individual drugs prescribed"""
    __tablename__ = 'drug_prescriptions'

    drug_id = Column(String(60),
                     ForeignKey('drugs.id', ondelete='CASCADE'),
                     nullable=False)
    prescription_id = Column(String(60),
                             ForeignKey('prescriptions.id',
                                        ondelete='CASCADE'),
                             nullable=False)
    dose = Column(String(16))
    frequency = Column(String(16))
    duration = Column(String(16))
    route = Column(String(16))
    prescription = relationship('Prescription', back_populates='drugs')
