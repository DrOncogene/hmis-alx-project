#!/usr/bin/python3
"""Module for Prescription class."""

from models.base_model import BaseModel


class Prescription(BaseModel):
    """Class representing a Prescription."""
    pid = ""
    consultation_id = ""
    drug_id = ""
    dose = ""
    unit = ""
    frequency = ""
    duration = ""
    period = ""
    route = ""
    dispensed_by = ""
