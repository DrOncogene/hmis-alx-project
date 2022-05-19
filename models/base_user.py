#!/usr/bin/python3
"""Module for BaseUser class"""

from models.base_model import BaseModel
from datetime import date


class BaseUser(BaseModel):
    """Class representing a BaseUser."""
    first_name = ""
    last_name = ""
    gender = ""
    email = ""
    date_of_birth = 0
    marital_status = ""
    address = ""
    telephone_number = 0
    kinfirst_name = ""
    kinlast_name = ""
    kincontact_address = ""
