#!/usr/bin/python3
"""This module instantiates a storage object"""
from os import getenv as osgetenv
from models.patient import Patient


if osgetenv('STORAGE_TYPE') == 'db':
    from storage.dbs import DBStorage
    storage = DBStorage()
else:
    from storage.fs import FileStorage
    storage = FileStorage()

# reload first
storage.reload()

if osgetenv('STORAGE_TYPE') != 'db':
    titles = ['Doctor', 'Nurse', 'Pharmacist', 'RecordOfficer', 'Admin']
    all_obj = storage.all()

    # then computes and store already existing ids
    staff_ids = [staff.staff_id for staff in all_obj.values()
                 if staff.__class__.__name__ in titles]
    patients = storage.all(Patient)
    pids = [patient.pid for patient in patients.values()]
