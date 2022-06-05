#!/usr/bin/python3
"""Module for Prescription class."""
from models.base_model import BaseModel


class Prescription(BaseModel):
    """Class representing a Prescription."""
    pid = ""
    consultation_id = ""
    drug_ids = [] # list of drug prescription ids
    dispensed_by = ""


class DrugPrescription(BaseModel):
    """represents a single drug prescibed"""
    drug_id = ""
    dose = ""
    frequency = ""
    duration = ""
    route = ""
