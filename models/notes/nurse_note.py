#!/usr/bin/python3
"""Module for NursesNote class."""

from models.base_model import BaseModel


class NurseNote(BaseModel):
    """Class representing a nurse note."""
    text = ""
