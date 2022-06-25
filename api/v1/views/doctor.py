#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Doctors """
from flask import jsonify
from flasgger.utils import swag_from

from models.notes.doctor import Doctor
from storage import storage
from api.v1.views import app_views


@app_views.route('/staffs/doctors/<string:staff_id>/consultations',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/doctors/staff_id/get_consultations.yml')
def get_consultations(staff_id):
    """ Retrieves the list of a doctor consultations """
    staff_id = int(staff_id[3:])
    doctor = storage.get(Doctor, 'staff_id', staff_id)

    if not doctor:
        abort(404, description="Staff does not exist")

    consultations = [consult.to_dict() for consult in doctor.consultations]

    return jsonify(consultations)


@app_views.route('/staffs/doctor/<string:staff_id>/prescriptions', 
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/doctors/staff_id/get_prescriptions.yml')
def get_prescriptions(staff_id):
    """ Retrieves the list of a doctor prescriptions """
    staff_id = int(staff_id[3:])
    doctor = storage.get(Doctor, 'staff_id', staff_id)

    if not doctor:
        abort(404, description="Staff does not exist")

    prescriptions = [prescription.to_dict()
                     for prescription in doctor.prescriptions]
    return jsonify(prescriptions)
