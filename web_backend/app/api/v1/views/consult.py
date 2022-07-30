#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Consultations """
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from flask_login import login_required, current_user

from models.patient import Patient
from models.notes.consult import Consultation
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/patients/<int:pid>/consultations', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/get_consultations.yml')
@RBAC.allow(['doctor', 'nurse'], methods=['GET'])
@login_required
def get_consultations(pid):
    """
    Retrieves the all consultation object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultations = [consult.to_dict() for consult in patient.consultations]
    return jsonify(consultations)


@api_views.route('/patients/<int:pid>/consultations/<string:consultation_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/consultations/get_consultation.yml')
@RBAC.allow(['doctor', 'nurse'], methods=['GET'])
@login_required
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


@api_views.route('/patients/<int:pid>/consultations/<string:consultation_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/consultations/delete_consulation.yml',
           methods=['DELETE'])
@RBAC.allow(['doctor'], methods=['DELETE'])
@login_required
def delete_consulation(pid, consultation_id):
    """
    Deletes a Consulation Object for a specific patient
    """
    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description='Consultation does not exist')

    if current_user.staff_id != consultation.created_by:
        abort(403)

    storage.delete(consultation)
    storage.save()

    return jsonify({}), 200


@api_views.route('/patients/<int:pid>/consultations',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/consultations/post_consultation.yml',
           methods=['POST'])
@RBAC.allow(['doctor'], methods=['POST'])
@login_required
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
    data['created_by'] = current_user.staff_id
    instance = Consultation(**data)
    instance.save()
    instance = storage.get('Consultation', 'id', instance.id)
    return make_response(jsonify(instance.to_dict()), 201)


@api_views.route('/patients/<int:pid>/consultations/<string:consultation_id>',
                 methods=['PUT'], strict_slashes=False)
@swag_from('documentation/consultations/put_consultation.yml', methods=['PUT'])
@RBAC.allow(['doctor'], methods=['PUT'])
@login_required
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

    if current_user.staff_id != consultation.created_by:
        abort(403)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(consultation, key, value)
    storage.save()
    consultation = storage.get('Consultation', 'id', consultation.id)
    return jsonify(consultation.to_dict())
