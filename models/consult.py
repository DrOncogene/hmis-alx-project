#!/usr/bin/python3
"""Module for Consultation class."""

from models.base_model import BaseModel


class Consult(BaseModel):
    """Class representing a Consultation"""
    patient_id = ""
    prescription_id = []
    vitals_id = []
    pc = ""
    hpc = ""
    pohx = None
    pghx = None
    pmhx = None
    prov_diag = None
    plan = None
