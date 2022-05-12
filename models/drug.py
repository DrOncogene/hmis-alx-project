#!/usr/bin/python3
"""Module for Drug class."""

from models.base_model import BaseModel


class Drug(BaseModel):
    """Class representing a Drug."""
    name = ""
    brand = ""
    route = ""
    formulation = ""
    expiry_date = 0
    stock_date = 0

