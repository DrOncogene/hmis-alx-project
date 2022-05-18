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
from models.notes.nursesnote import NursesNote
from models.drug import Drug

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from storage.dbs import DBStorage
    storage = DBStorage()
else:
    from storage.fs import FileStorage
    storage = FileStorage()


storage.reload()
