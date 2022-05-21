#!usr/bin/pyhton3
""" A class Admin that inherits from Staff """


from models.staff import Staff
from datetime import date


class Admin(Staff, Permissions):
    """ Simple Admin class model """
    pass
