#!/usr/bin/python3
"""Module for Drug class."""

from models.base_model import BaseModel
from datetime import date


class Drug(BaseModel):
    """Class representing a Drug."""
    name = ""
    dose = ""
    route = ""
    brand = ""
    formulation = ""
    expiry_date = 0
    stock_date = 0