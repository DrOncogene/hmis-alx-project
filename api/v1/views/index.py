#!/usr/bin/python3
""" Index """
from flask import jsonify

from api.v1.views import app_views
from models.admin import Admin
from models.doctor import Doctor
from models.nurse import Nurse
from models.patient import Patient
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.drug import Drug
from models.notes.consult import Consultation
from models.notes.prescription import Prescription
from models.notes.vitals import VitalSign
from models.notes.nursenote import NurseNote
from storage import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = {
       "patient": Patient,
       "doctor": Doctor,
       "nurse": Nurse,
       "pharmacist": Pharmacist,
       "recordofficer": RecordOfficer,
       "admin": Admin,
       "drug": Drug,
       "consultation": Consultation,
       "prescription": Prescription,
       "vital": VitalSign,
       "nursenote": NurseNote
    }

    num_objs = {}
    for name, cls in classes.items():
        num_objs[name] = storage.count(cls)

    return jsonify(num_objs)
