#!usr/bin/pyhton3
""" A class Doctor that inherits from Staff """
from models.staff import Staff
from models.permissions import Permission


class Doctor(Staff):
    """ Simple Doctor class model """
    job_title = "Doctor"
    permissions = Permission(
        create = ('consultation', 'prescription'),
        edit = ('consultation', 'prescription'),
        delete = ('consultation', 'prescription'),
        view = ('all')
    )

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            # if it's a new instantiation, generate a staff_id
            super().set_staff_id()
