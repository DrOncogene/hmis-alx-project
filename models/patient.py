#!/usr/bin/python3
"""Module for Patient class."""

from models.base_model import BaseModel
from datetime import datetime


class Patient(BaseModel):
    """Class representing a Patient."""
    first_name = ""
    last_name = ""
    hospital_number = 0
    gender = ""
    email = ""
    date_of_birth = 0
    marital_status = ""
    address = ""
    kinfirst_name = ""
    kinlast_name = ""
    consult_id = []
    prescription_id = []
    vitals_id = []