#!usr/bin/pyhton3
""" A class Records that inherits from Staff """

from models.staff import Staff


class RecordOfficer(Staff):
    """ Simple RecordOfficer class model """
    job_title = "RecordOfficer"

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
