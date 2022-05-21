#!usr/bin/pyhton3
""" A class Staff that inherits from BaseUser """


from models.base_user import BaseUser
from models.permissions import Permissions
from datetime import date


class Staff(BaseUser, Permissions):
    """ Simple Staff class model """

    __number_staffs = 0

    """def __init__(self, id=None, *args, **kwargs):
        super().__init__()
        self.id = id
        if self.id is None:
            self.__number_staffs += 1
            self.id = self.__number_staffs
        self.id = str(self.id + 1)"""
    staff_id = 0
    job_title = ""
