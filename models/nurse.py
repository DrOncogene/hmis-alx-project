#!usr/bin/pyhton3
""" A class Nurse that inherits from Staff """


from models.staff import Staff
from datetime import date


class Nurse(Staff, Permissions):
    """ Simple Nurse class model """
    pass
