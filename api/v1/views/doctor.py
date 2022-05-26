#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Doctors """
from models.notes.consult import Consultation
from models.notes.prescription import Prescription
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/staffs/doctor/<staff_id>/consultations', methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/doctor/staff_id/get_consultations.yml')
def get_consultations(staff_id):
    """ Retrieves the list of a doctor consultations """
    all_consultations = storage.all(Consultation).values()
    doctor_consultations = []
    for consultation in all_consultations:
        if consultation.created_by == staff_id:
            doctor_consultations.append(consultation.to_dict())
    return jsonify(doctor_consultations)


@app_views.route('/staffs/doctor/<staff_id>/prescriptions', methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/doctor/staff_id/get_prescriptions.yml')
def get_prescriptions(staff_id):
    """ Retrieves the list of a doctor prescriptions """
    all_prescriptions = storage.all(Prescription).values()
    doctor_prescriptions = []
    for prescription in all_prescriptions:
        if prescription.created_by == staff_id:
            doctor_prescriptions.append(prescription.to_dict())
    return jsonify(doctor_prescriptions)
