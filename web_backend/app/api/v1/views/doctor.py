#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Doctors """
from flask import jsonify, abort
from flasgger.utils import swag_from
from flask_login import login_required

from models.doctor import Doctor
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/staffs/doctors/<string:staff_id>/consultations',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/doctors/staff_id/get_consultations.yml')
@RBAC.allow(['doctors'], methods=['GET'])
@login_required
def get_doctor_consultations(staff_id):
    """ Retrieves the list of a doctor consultations """
    staff_id = int(staff_id[3:])
    doctor = storage.get(Doctor, 'staff_id', staff_id)

    if not doctor:
        abort(404, description="Staff does not exist")

    consultations = [consult.to_dict()
                     for consult in doctor.consultations]
    return jsonify(consultations)


@api_views.route('/staffs/doctors/<string:staff_id>/prescriptions',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/doctors/staff_id/get_prescriptions.yml')
@RBAC.allow(['doctor'], methods=['GET'])
@login_required
def get_doctor_prescriptions(staff_id):
    """ Retrieves the list of a doctor prescriptions """
    staff_id = int(staff_id[3:])
    doctor = storage.get(Doctor, 'staff_id', staff_id)

    if not doctor:
        abort(404, description="Staff does not exist")

    prescriptions = [prescription.to_dict()
                     for prescription in doctor.prescriptions]
    return jsonify(prescriptions)
