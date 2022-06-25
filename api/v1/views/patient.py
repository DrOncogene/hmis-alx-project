#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Patients """
from models.patient import Patient
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/patients', methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/all_patients.yml')
def get_patients():
    """ Retrieves the list of all patient object or a specific patient """
    all_patients = storage.all(Patient)
    return jsonify(all_patients)


@app_views.route('/patients/<pid>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/get_patients.yml', methods=['GET'])
def get_patient(pid):
    """ Retrieves an patient """
    patient = storage.get(Patient, 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    return jsonify(patient.to_dict())


@app_views.route('/patients/<pid>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patients/delete_patient.yml', methods=['DELETE'])
def delete_patient(pid):
    """
    Deletes a patient Object
    """
    patient = storage.get(Patient, 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    storage.delete(patient)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients', methods=['POST'], strict_slashes=False)
@swag_from('documentation/patients/post_patient.yml', methods=['POST'])
def post_patient():
    """
    Creates a patient
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'first_name' not in request.get_json():
        abort(400, description="Missing first name")
    if 'last_name' not in request.get_json():
        abort(400, description="Missing last name")
    if 'gender' not in request.get_json():
        abort(400, description="Missing gender")
    if 'dob' not in request.get_json():
        abort(400, description="Missing date of birth")
    if 'marital_status' not in request.get_json():
        abort(400, description="Missing marital status")
    if 'address' not in request.get_json():
        abort(400, description="Missing address")
    if 'phone_number' not in request.get_json():
        abort(400, description="Missing phone number")
    if 'next_of_kin' not in request.get_json():
        abort(400, description="Missing next of kin")
    if 'kin_address' not in request.get_json():
        abort(400, description="Missing next of kin address")

    data = request.get_json()
    instance = Patient(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/patients/<pid>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/patients/put_patient.yml', methods=['PUT'])
def put_patient(pid):
    """
    Updates a patient
    """
    patient = storage.get(Patient, 'pid', pid)

    if not patient:
        abort(404, description="Patient not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(patient, key, value)
    storage.save()
    return make_response(jsonify(patient.to_dict()), 200)
