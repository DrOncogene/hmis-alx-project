#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Vital Signs """
from flasgger.utils import swag_from
from flask import abort, jsonify, make_response, request
from flask_login import current_user, login_required

from models.notes.vitals import VitalSign
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/patients/<int:pid>/vitals', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/patients/get_vitals.yml')
@RBAC.allow(['nurse'], methods=['GET'])
@login_required
def get_vitals(pid):
    """
    Retrieves the all VitalSign object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    vitals = [vitals.to_dict() for vitals in patient.vitals]
    return jsonify(vitals)


@api_views.route('/patients/<int:pid>/vitals/<vitals_id>', methods=['GET'],
                 defaults={'consult_id': None}, strict_slashes=False)
@api_views.route('/patients/<int:pid>/consultations/<consult_id>/vitals',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/vitals/get_vital.yml')
@RBAC.allow(['nurse'], methods=['GET'])
@login_required
def get_vital(pid, consult_id, vitals_id=None):
    """
    Retrieves the vitals for a consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    if consult_id is not None:
        consultation = storage.get('Consultation', 'id', consult_id)
        if (not consultation) or (consultation.pid != pid):
            abort(404, description="Consultation not found")

    if vitals_id is not None:
        vitals = storage.get(VitalSign, 'id', vitals_id)
        if not (vitals or vitals in patient.vitals):
            abort(404, description="No such vitals")
    else:
        vitals = consultation.vitals

    if not vitals:
        abort(404, description="No such vitals")

    return jsonify(vitals.to_dict())


@api_views.route('/patients/<int:pid>/vitals/<vitals_id>', methods=['DELETE'],
                 defaults={'consult_id': None}, strict_slashes=False)
@api_views.route('/patients/<int:pid>/consultations/<consult_id>/vitals',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patients/vitals/delete_vitals.yml',
           methods=['DELETE'])
@RBAC.allow(['nurse'], methods=['DELETE'])
@login_required
def delete_vitals(pid, consult_id, vitals_id=None):
    """
    Deletes the vitals for a consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    if consult_id is not None:
        consultation = storage.get('Consultation', 'id', consult_id)
        if (not consultation) or (consultation.pid != pid):
            abort(404, description="Consultation not found")

    if vitals_id is not None:
        vitals = storage.get(VitalSign, 'id', vitals_id)
        if not (vitals or vitals in patient.vitals):
            abort(404, description="No such vitals")
    else:
        vitals = consultation.vitals

    if not vitals:
        abort(404, description="No such vitals")

    if vitals.created_by != current_user.staff_id:
        abort(403)

    storage.delete(vitals)
    storage.save()

    return make_response(jsonify({}), 200)


@api_views.route('/patients/<int:pid>/vitals',
                 methods=['POST'], strict_slashes=False)
@api_views.route('/patients/<int:pid>/<consult_id>/vitals',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patients/vitals/post_vitals.yml', methods=['POST'])
@RBAC.allow(['nurse'], methods=['POST'])
@login_required
def post_vitals(pid, consult_id=None):
    """
    Creates a new vitals for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    if consult_id is not None:
        consultation = storage.get('Consultation', 'id', consult_id)
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
    if consult_id is not None:
        data['consultation_id'] = consult_id
    data['created_by'] = current_user.staff_id
    vitals = VitalSign(**data)
    vitals.save()
    vitals = storage.get('VitalSign', 'id', vitals.id)
    return make_response(jsonify(vitals.to_dict()), 201)


@api_views.route('/patients/<int:pid>/vitals/<vitals_id>', methods=['PUT'],
                 defaults={'consult_id': None}, strict_slashes=False)
@api_views.route('/patients/<int:pid>/<consult_id>/vitals', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/patients/vitals/put_vitals.yml', methods=['PUT'])
@RBAC.allow(['nurse'], methods=['PUT'])
@login_required
def put_vitals(pid, consult_id, vitals_id=None):
    """
    Updates a vitals for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    if consult_id is not None:
        consultation = storage.get('Consultation', 'id', consult_id)
        if (not consultation) or (consultation.pid != pid):
            abort(404, description="Consultation not found")

    if vitals_id is not None:
        vitals = storage.get(VitalSign, 'id', vitals_id)
        if not (vitals or vitals in patient.vitals):
            abort(404, description="No such vitals")
    else:
        vitals = consultation.vitals

    if not vitals:
        abort(404, description='No such vitals')

    if vitals.created_by != current_user.staff_id:
        abort(403)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(vitals, key, value)

    vitals.save()
    vitals = storage.get('VitalSign', 'id', vitals.id)

    return make_response(jsonify(vitals.to_dict()), 200)
