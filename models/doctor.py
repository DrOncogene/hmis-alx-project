#!usr/bin/pyhton3
""" A class Doctor that inherits from Staff """


from models.staff import Staff
from datetime import date


class Doctor(Staff, Permissions):
    """ Simple Doctor class model """
    pass
