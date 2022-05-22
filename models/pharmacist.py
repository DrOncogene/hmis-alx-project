#!usr/bin/pyhton3
""" A class Pharmacist that inherits from Staff """
from models.staff import Staff
from models.permissions import Permission


class Pharmacist(Staff):
    """ Simple Pharmacist class model """
    job_title = "Pharmacist"
    permissions = Permission(
        create = ('Drug'),
        edit = ('prescription', 'Drug'),
        delete = ('Drug'),
        view = ('prescription', 'Drug')
    )

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
