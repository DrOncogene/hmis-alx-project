#!/usr/bin/python3
"""Module for Consultation class."""
from models.base_model import BaseModel


class Consultation(BaseModel):
    """Class representing a Consultation"""
    pid = ""
    prescription_ids = []
    vitals_ids = []
    pc = ""
    hpc = ""
    pohx = ""
    pghx = ""
    pmhx = ""
    prov_diag = ""
    plan = ""
