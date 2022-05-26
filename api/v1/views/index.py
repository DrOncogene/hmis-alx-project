#!/usr/bin/python3
""" Index """
from models.patient import Patient
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from storage import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Patient, Doctor, Nurse, Pharmacist, RecordOfficer, Admin]
    names = ["patient", "doctor", "nurse", "pharmacist", "recordofficer", "admin"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
