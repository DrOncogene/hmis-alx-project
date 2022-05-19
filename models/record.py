#!/usr/bin/python3
"""Defines the RecordOfficer class"""

from models.staff import Staff


class RecordOfficer(Staff):
    """Defines a record officer object"""
    job_title = "RecordOfficer"
    permissions = ""

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
