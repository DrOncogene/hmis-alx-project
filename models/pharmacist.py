#!usr/bin/pyhton3
""" A class Pharmacist that inherits from Staff """


from models.staff import Staff
from datetime import date


class Pharmacist(Staff, Permissions):
    """ Simple Pharmacist class model """
    pass
