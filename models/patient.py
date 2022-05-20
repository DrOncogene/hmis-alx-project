#!/usr/bin/python3
"""Module for Patient class."""

from models.base_user import BaseUser
from datetime import date


class Patient(BaseUser):
    """Class representing a Patient."""
    pid = ""
    consult_id = []
    prescription_id = []
    vitals_id = []
