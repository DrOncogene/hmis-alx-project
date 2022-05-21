#!usr/bin/pyhton3
""" A class Nurse that inherits from Staff """

from models.staff import Staff


class Nurse(Staff, Permission):
    """ Simple Nurse class model """
    job_title = "Nurse"

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
