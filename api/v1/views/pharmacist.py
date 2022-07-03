#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Pharmacist """
from flask import jsonify, abort
from flasgger.utils import swag_from

from models.pharmacist import Pharmacist
from storage import storage
from api.v1.views import app_views


@app_views.route('/staffs/pharmacists/<string:staff_id>/prescriptions', methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/pharmacist/staff_id/get_prescriptions.yml')
def get_pharmacist_prescriptions(staff_id):
    """ Retrieves the list of a pharmacist dispensed prescriptions """

    staff_id = int(staff_id[3:])
    pharmacist = storage.get(Pharmacist, 'staff_id', staff_id)
    if not pharmacist:
        abort(404, description="Staff does not exist")

    prescriptions = [prescription.to_dict()
                     for prescription in pharmacist.prescriptions]
    return jsonify(prescriptions)
