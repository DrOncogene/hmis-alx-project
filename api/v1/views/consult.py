#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Consultations """
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

from models.patient import Patient
from storage import storage
from api.v1.views import app_views


@app_views.route('/patients/<int:pid>/consultations', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/get_consultations.yml')
def get_consultations(pid):
    """
    Retrieves the all consultation object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultations = [consult.to_dict() for consult in patient.consultations]
    return jsonify(consultations)


@app_views.route('/patients/<int:pid>/consultations/<string:consultation_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/get_consultation.yml')
def get_consultation(pid, consultation_id):
    """
    Retrieves the a specific consultation object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description='Consultation does not exist')

    return jsonify(consultation.to_dict())


@app_views.route('/patients/<int:pid>/consutations/<string:consultation_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/delete_consulation.yml',
           methods=['DELETE'])
def delete_consulation(pid, consultation_id):
    """
    Deletes a Consulation Object for a specific patient
    """
    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description='Consultation does not exist')

    storage.delete(consultation)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<int:pid>/consultations',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/post_consultation.yml', methods=['POST'])
def post_consultation(pid):
    """
    Creates a new consultation for a specific patient
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'prov_diag' not in request.get_json():
        abort(400, description="Missing diagnosis")

    patient = storage.get(Patient, 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    data = request.get_json()
    data['pid'] = pid
    instance = 'Consultation'(**data)
    instance.save()
    instance = storage.get('Consultation', 'id', instance.id)
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/patients/<int:pid>/consultations/<string:consultation_id>',
                 methods=['PUT'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/put_consultation.yml', methods=['PUT'])
def put_consultation(pid, consultation_id):
    """
    Updates a consultation for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description='Consultation does not exist')

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(consultation, key, value)
    storage.save()
    consultation = storage.get('Consultation', 'id', consultation.id)
    return make_response(jsonify(consultation.to_dict()), 200)
