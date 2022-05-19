#!/usr/bin/python3
"""Defines the Doctor class"""

from models.staff import Staff


class Admin(Staff):
    """Defines a doctor object"""
    permissions = ""
