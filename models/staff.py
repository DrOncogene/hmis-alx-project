#!usr/bin/pyhton3
""" A class Staff that inherits from BaseUser """
from os import getenv as osgetenv
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_user import BaseUser


class Staff(BaseUser):
    """ Simple Staff class model """
    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def set_staff_id(self):
        """method to generate staff_id of a new staff in
        the format <TITLE><4-DIGITSERIAL_NUM> e.g. DOC0001"""
        from storage import staff_ids
        titles = {
            "Admin": "ADM",
            "Doctor": "DOC",
            "Nurse": "NRS",
            "Pharmacist": "PHM",
            "RecordOfficer": "REC"
        }
        # get the short title according to the class
        # of the current object
        title = titles[self.__class__.__name__]
        try:
            # retrieve all staff ids from the id store in storage
            # and filter by the current title
            cls_ids = [staff_id for staff_id in staff_ids
                       if title in staff_id]
            # slice out the titles from the staff_ids to get only
            # the numbers
            id_nums = [int(num[3:]) for num in cls_ids]
            # sort the numbers and get the last one
            last = sorted(id_nums)[-1]
            # set the current obj staff_id to title + last num + 1
            self.staff_id = "{}{:04}".format(title, last + 1)
        except IndexError:
            # if there is no staff obj of the current in store
            # set staff_id to title + 0000
            self.staff_id = "{}{:04}".format(title, 0)
        # add the new staff_id to the staff_ids store
        staff_ids.append(self.staff_id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
