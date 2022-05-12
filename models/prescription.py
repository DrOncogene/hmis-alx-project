#!/usr/bin/python3
"""Module for Prescription class."""

from models.base_model import BaseModel


class Prescription(BaseModel):
    """Class representing a Prescription."""
    patient_id = ""
    consult_id = []
    drug_id = None
    dose = 0
    unit = ""
    frequency = ""
    duration = ""
    period = ""
    route = ""
    dispensed by = staff_id
