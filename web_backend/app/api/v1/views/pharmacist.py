#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Pharmacist """
from flask import jsonify, abort
from flasgger.utils import swag_from
from flask_login import login_required

from models.pharmacist import Pharmacist
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/staffs/pharmacists/<string:staff_id>/prescriptions',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/pharmacist/staff_id/get_prescriptions.yml')
@RBAC.allow(['pharmacist'], methods=['GET'])
@login_required
def get_pharmacist_prescriptions(staff_id):
    """ Retrieves the list of a pharmacist dispensed prescriptions """

    staff_id = int(staff_id[3:])
    pharmacist = storage.get(Pharmacist, 'staff_id', staff_id)
    if not pharmacist:
        abort(404, description="Staff does not exist")

    prescriptions = [prescription.to_dict()
                     for prescription in pharmacist.prescriptions]
    return jsonify(prescriptions)
