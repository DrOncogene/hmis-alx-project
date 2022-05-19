#!/usr/bin/python3
"""Module for Vital Signs class."""

from models.base_model import BaseModel


class VitalSign(BaseModel):
    """Class representing Vital signs."""
    patient_id = ""
    consult_id = ""
    pr = None
    rr = None
    bp = None
    temp = None
    spo2 = None
    height = None
    weight = None
