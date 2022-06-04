#!/usr/bin/python3
"""Module for Patient class."""
from os import getenv as osgetenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_user import BaseUser
from models.base_model import Base


class Patient(BaseUser, Base):
    """Class representing a Patient."""
    __tablename__ = 'patients'

    if osgetenv('STORAGE_TYPE') == 'db':
        pid = Column(Integer, primary_key=True, autoincrement=True)
        consultations = relationship('Consultation', cascade='all, delete',
                                     back_populates='patient')
        prescriptions = relationship('Prescription', cascade='all, delete',
                                     back_populates='patient')
        vitals = relationship('VitalSign', cascade='all, delete',
                              back_populates='patient')
        nursenotes = relationship('NurseNote', cascade='all, delete',
                                  back_populates='patient')
    else:
        pid = ""
        consultation_ids = []
        prescription_ids = []
        vitals_ids = []

    def __init__(self, **kwargs):
        if (kwargs):
            super().__init__(**kwargs)
        else:
            super().__init__()

        if osgetenv('STORAGE_TYPE') != 'db':
            from storage import pids as pid_store
            try:
                # grab all the pids in the store and convert to numbers
                pids = [int(pid) for pid in pid_store]
                # sort them and grab the last one
                print(pids)
                last = sorted(pids)[-1]
                # set current pid to last + 1 in 8 digits
                self.pid = "{:08}".format(last + 1)
            except IndexError:
                # if no existing pids, set to 0 in 8 digits
                self.pid = "{:08}".format(0)
            # add the new pid to the pids store
            pid_store.append(self.pid)
