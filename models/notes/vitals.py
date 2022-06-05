#!/usr/bin/python3
"""Module for Vital Signs class."""
from models.base_model import BaseModel


class VitalSign(BaseModel):
    """Class representing Vital signs."""
    pid = ""
    consultation_id = ""
    pr = 0
    rr = 0
    sbp = 0
    dbp = 0
    temp = 0
    spo2 = 0
    height = 0
    weight = 0
