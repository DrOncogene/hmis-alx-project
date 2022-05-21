#!usr/bin/pyhton3
""" A class Admin that inherits from Staff """

from models.staff import Staff


class Admin(Staff):
    """ Simple Admin class model """
    job_title = "Admin"

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
