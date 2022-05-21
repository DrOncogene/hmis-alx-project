#!/usr/bin/python3
"""Defines the Nurse class"""
from models.staff import Staff


class Nurse(Staff):
    """Defines a nurse object"""
    job_title = "Nurse"
    permissions = ""

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
