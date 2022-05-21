#!/usr/bin/python3
"""Module for Nurse Note class."""

from models.base_model import BaseModel


class NurseNote(BaseModel):
    """Class representing a Nurse Note"""
    pid = ""
    vitals_ids = []
    note = ""