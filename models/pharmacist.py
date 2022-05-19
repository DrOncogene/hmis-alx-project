#!/usr/bin/python3
"""Defines the Pharmacist class"""

from models.staff import Staff


class Pharmacist(Staff):
    """Defines a pharmacist object"""
    job_title = "Pharmacist"
    permissions = ""

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
