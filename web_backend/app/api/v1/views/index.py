#!/usr/bin/python3
""" Index """
from flask import jsonify
from flask_login import login_required

from models.admin import Admin
from models.doctor import Doctor
from models.nurse import Nurse
from models.patient import Patient
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from storage import storage
from . import api_views


@api_views.route('/status', methods=['GET'], strict_slashes=False)
@login_required
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@api_views.route('/stats', methods=['GET'], strict_slashes=False)
@login_required
def stats_by_type():
    """ Retrieves the number of each objects by type """
    classes = {
       "patient": Patient,
       "doctor": Doctor,
       "nurse": Nurse,
       "pharmacist": Pharmacist,
       "recordofficer": RecordOfficer,
       "admin": Admin,
    }

    num_objs = {}
    for name, cls in classes.items():
        num_objs[name] = storage.count(cls)

    return jsonify(num_objs)
