#!/usr/bin/python3
"""Module for Permissions class."""

from models.base_model import BaseModel


class Permission(BaseModel):
    """Class representing a Permissions."""
    __items = []
    __create = ""
    __edit = ""
    __delete = ""
    __view = ""
