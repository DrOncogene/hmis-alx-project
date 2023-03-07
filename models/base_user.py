#!/usr/bin/python3
"""Module for BaseUser class."""
from sqlalchemy import Column, String, Enum, Date
from models.base_model import BaseModel


class BaseUser(BaseModel):
    """Class representing a BaseUser."""

    first_name = Column(String(128))
    last_name = Column(String(128))
    other_names = Column(String(128), default='')
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

    def get_full_name(self):
        """return the full name"""
        full_name = f'{self.first_name} {self.last_name} {self.other_names}'
        return full_name
