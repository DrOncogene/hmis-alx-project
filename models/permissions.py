#!/usr/bin/python3
"""Module for Permissions class
Contains the Permissions class for the HMIS console.
"""

from datetime import datetime
from models.base_model import BaseModel


class Permissions(BaseModel):
    """Class for permissions of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Permissions instance"""
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
        __items = []
        __create = ""
        __edit = ""
        __delete = ""
        __view = ""
