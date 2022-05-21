#!/usr/bin/python3
"""Module for Patient class."""
from models.base_user import BaseUser
import storage


class Patient(BaseUser):
    """Class representing a Patient."""
    pid = ""
    consultation_ids = []
    prescription_ids = []
    vitals_ids = []

    def __init__(self, **kwargs):
        if (kwargs):
            super().__init__(**kwargs)
        else:
            super().__init__()

        try:
            # grab all the pids in the store and convert to numbers
            pids = [int(num) for num in storage.pids]
            # sort them and grab the last one
            last = sorted(pids)[-1]
            # set current pid to last + 1 in 8 digits
            self.pid = "{:08}".format(last + 1)
        except IndexError:
            # if no existing pids, set to 0 in 8 digits
            self.pid = "{:08}".format(0)
        # add the new pid to the pids store
        storage.pids.append(self.pid)
