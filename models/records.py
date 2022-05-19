#!usr/bin/pyhton3
""" A class Records that inherits from Staff """


from models.staff import Staff
from datetime import date


class Records(Staff, Permissions):
    """ Simple Records class model """
    pass
