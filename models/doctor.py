#!/usr/bin/python3
"""Defines the Doctor class"""
from models.staff import Staff


class Doctor(Staff):
    """Defines a doctor object"""
    job_title = "Doctor"
    permissions = ""

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            # if it's a new instantiation, generate a staff_id
            super().set_staff_id()
