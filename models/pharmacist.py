#!usr/bin/pyhton3
""" A class Pharmacist that inherits from Staff """

from models.staff import Staff


class Pharmacist(Staff):
    """ Simple Pharmacist class model """
    job_title = "Pharmacist"

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
