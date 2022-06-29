#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Vital Signs """
from flasgger.utils import swag_from
from flask import abort, jsonify, make_response, request

from models.notes.vitals import VitalSign
from storage import storage
from api.v1.views import app_views


@app_views.route('/patients/<int:pid>/vitals', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/get_vitals.yml')
def get_vitals(pid):
    """
    Retrieves the all VitalSign object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    vitals = [vitals.to_dict() for vitals in patient.vitals]
    return jsonify(vitals)


@app_views.route('/patients/<int:pid>/consultations/<consultation_id>/vitals',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultations/consultation_id/get_vital.yml')
def get_consult_vitals(pid, consultation_id):
    """
    Retrieves the all vital object for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'pid', pid)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    vitals = [vitals.to_dict() for vitals in consultation.vitals]
    return jsonify(vitals)


@app_views.route('/patients/<int:pid>/consultations/<consultation_id>/vitals/<vital_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultations/consultation_id/vitals/get_vital.yml')
def get_vital(pid, consultation_id, vital_id):
    """ Retrieves the a specific vital object for a specific consultation """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    vital = storage.get('VitalSign', 'id', vital_id)
    if not vital:
        abort(404, description="No such vitals")

    return jsonify(vital.to_dict())


@app_views.route('/patients/<int:pid>/consultations/<consultation_id>/vitals/<vitals_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultation/consultation_id/vitals/delete_vitals.yml',
           methods=['DELETE'])
def delete_vitals(pid, consultation_id, vital_id):
    """
    Deletes a VitalSign Object for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    vitals = storage.get('VitalSign', 'id', vital_id)
    if not vitals:
        abort(404, description="No such vitals")

    storage.delete(vitals)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<int:pid>/<consultation_id>',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/post_vitals.yml', methods=['POST'])
def post_vitals(pid, consultation_id, vital_id):
    """
    Creates a new vitals for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'pr' not in request.get_json():
        abort(400, description="Missing pulse rate")
    if 'rr' not in request.get_json():
        abort(400, description="Missing respiratory rate")
    if 'bp' not in request.get_json():
        abort(400, description="Missing blood pressure")
    if 'temp' not in request.get_json():
        abort(400, description="Missing temperature")

    data = request.get_json()
    data['pid'] = pid
    data['consultation_id'] = consultation_id
    instance = VitalSign(**data)
    instance.save()
    instance = storage.get('VitalSign', 'id', instance.id)
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/patients/<int:pid>/<consultation_id>/<vitals_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/put_vitals.yml',
           methods=['PUT'])
def put_vitals(pid, consultation_id, vitals_id):
    """
    Updates a vitals for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    vitals = storage.get('VitalSign', 'id', vitals_id)
    if not vitals:
        abort(404, description='No such vitals')

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(vitals, key, value)

    storage.save()
    vitals = storage.get('VitalSign', 'id', vitals.id)
    return make_response(jsonify(vitals.to_dict()), 200)
