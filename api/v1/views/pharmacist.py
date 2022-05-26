#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Pharmacist """
from models.notes.prescription import Prescription
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/staffs/pharmacist/<staff_id>/prescriptions', methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/pharmacist/staff_id/get_prescriptions.yml')
def get_prescriptions(staff_id):
    """ Retrieves the list of a pharmacist dispensed prescriptions """
    all_prescriptions = storage.all(Prescription).values()
    pharmacist_prescriptions = []
    for prescription in all_prescriptions:
        if prescription.dispensed_by == staff_id:
            pharmacist_prescriptions.append(prescription.to_dict())
    return jsonify(pharmcist_prescriptions)
