#!/usr/bin/python3
"""Module for Drug class."""
from models.base_model import BaseModel
from datetime import date


class Drug(BaseModel):
    """Class representing a Drug."""
    name = ""
    dose = ""
    unit = ""
    route = ""
    brand = ""
    formulation = ""
    #Difficulty with deciding how to manage the dispensary system for the drugs shelf life
    #expiry_date = ""
    #stock_date = ""
