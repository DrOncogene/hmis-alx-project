#!/usr/bin/python3
"""Module for BaseUser class."""
from models.base_model import BaseModel
from datetime import date


class BaseUser(BaseModel):
    """Class representing a BaseUser."""
    first_name = ""
    last_name = ""
    gender = ""
    email = ""
    dob = ""
    marital_status = ""
    address = ""
    telephone_number = ""
    kinfirst_name = ""
    kinlast_name = ""
    kincontact_address = ""
