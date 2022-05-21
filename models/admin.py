#!usr/bin/pyhton3
""" A class Admin that inherits from Staff """

from models.staff import Staff


class Admin(Staff, Permissions):
    """ Simple Admin class model """
    pass
