#!usr/bin/pyhton3
""" A class Nurse that inherits from Staff """
from models.staff import Staff
from models.permissions import Permission


class Nurse(Staff):
    """ Simple Nurse class model """
    job_title = "Nurse"
    permissions = Permission(
        create = ('vitals', 'nursenote'),
        edit = ('vitals', 'nursenote'),
        delete = ('vitals', 'nursenote'),
        view = ('all')
    )

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
