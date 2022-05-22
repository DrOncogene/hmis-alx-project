#!usr/bin/pyhton3
""" A class Records that inherits from Staff """
from models.staff import Staff
from models.permissions import Permission


class RecordOfficer(Staff):
    """ Simple RecordOfficer class model """
    job_title = "RecordOfficer"
    permissions = Permission(
        create = ('patient'),
        edit = ('patient'),
        delete = (),
        view = ('patient')
    )

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            super().set_staff_id()
