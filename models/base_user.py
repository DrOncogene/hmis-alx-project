#!/usr/bin/python3
"""Module for BaseUser class."""
from os import getenv as osgetenv
from sqlalchemy import Column, String, Enum, Date
from models.base_model import BaseModel


class BaseUser(BaseModel):
    """Class representing a BaseUser."""

    if osgetenv('STORAGE_TYPE') == 'db':
        first_name = Column(String(128))
        last_name = Column(String(128))
        gender = Column(Enum('Male', 'Female',
                             validate_strings=True,
                             name='gender'))
        email = Column(String(128), unique=True)
        dob = Column(Date())
        marital_status = Column(Enum('Single', 'Married',
                                     'Widowed', 'Divorced',
                                     validate_strings=True,
                                     name='marital_status'))
        address = Column(String(128))
        phone_number = Column(String(16))
        next_of_kin = Column(String(128))
        kin_address = Column(String(128))
    else:
        first_name = ""
        last_name = ""
        gender = ""
        email = ""
        dob = ""
        marital_status = ""
        address = ""
        telephone_number = ""
        next_of_kin = ""
        kin_address = ""
