#!/usr/bin/python3
"""Module for Vital Signs class."""

from models.base_model import BaseModel


class VitalSign(BaseModel):
    """Class representing Vital signs."""
    pid = ""
    consultation_id = ""
    pr = ""
    rr = ""
    bp = ""
    temp = ""
    spo2 = ""
    height = ""
    weight = ""
