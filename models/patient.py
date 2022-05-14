#!/usr/bin/python3
"""Module for Patient class."""

from models.base_model import BaseModel
from datetime import date


class Patient(BaseModel):
    """Class representing a Patient."""
    first_name = ""
    last_name = ""
    hospital_number = ""
    gender = ""
    email = ""
    date_of_birth = date(0, 0, 0)
    marital_status = ""
    address = ""
    kinfirst_name = ""
    kinlast_name = ""
    consult_id = []
    prescription_id = []
    vitals_id = []