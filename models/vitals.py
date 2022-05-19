#!/usr/bin/python3
"""Module for Vital Signs class."""

from models.base_model import BaseModel


class Vitals(BaseModel):
    """Class representing Vital signs."""
    patient_id = ""
    consult_id = ""
    pr = ""
    rr = ""
    bp = ""
    temp = ""
    spo2 = ""
    height = ""
    weight = ""
