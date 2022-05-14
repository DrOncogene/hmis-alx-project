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
    date_of_birth = 0
    marital_status = ""
    address = ""
    telephone_number = 0
    kinfirst_name = ""
    kinlast_name = ""
    consult_id = []
    prescription_id = []
    vitals_id = []