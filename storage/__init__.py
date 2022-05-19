#!/usr/bin/python3
"""This module instantiates a storage object"""
import os
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from models.notes.consult import Consultation
from models.notes.prescription import Prescription
from models.notes.vitals import VitalSign
from models.notes.nurse_note import NurseNote
from models.drug import Drug

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from storage.dbs import DBStorage
    storage = DBStorage()
else:
    from storage.fs import FileStorage
    storage = FileStorage()

# create two id stores to hold staff ids and patient ids (pid)
staff_ids = []
pids = []
# reload first
storage.reload()

titles = ['Doctor', 'Nurse', 'Pharmacist', 'RecordOfficer']
all_obj = storage.all()

# then computes and store already existing ids
staff_ids = [staff.staff_id for staff in all_obj.values()
             if staff.__class__.__name__ in titles]
patients = storage.all('Patient')
pids = [patient.pid for patient in patients.values()]
