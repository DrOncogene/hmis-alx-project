#!usr/bin/pyhton3
""" A class Staff that inherits from BaseModel """


from models.base_model import BaseModel
from models import storage


class Staff(BaseModel):
    """ Simple Staff class model """

    __number_staffs = 0

    """def __init__(self, id=None, *args, **kwargs):
        super().__init__()
        self.id = id
        if self.id is None:
            self.__number_staffs += 1
            self.id = self.__number_staffs
        self.id = str(self.id + 1)"""
    first_name = ""
    last_name = ""
    gender = ""
    email = ""
    date_of_birth = 0
    marital_status = ""
    address = ""
    telephone_number = 0
    job_title = ""
