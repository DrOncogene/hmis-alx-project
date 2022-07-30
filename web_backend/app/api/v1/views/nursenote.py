#!/usr/bin/python3
""" objects that handle all default RestFul API actions for NurseNote """
from flasgger.utils import swag_from
from flask import abort, jsonify, request
from flask_login import login_required, current_user

from models.notes.nursenote import NurseNote
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/patients/<int:pid>/nursenotes',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/get_nursenotes.yml')
@RBAC.allow(['doctor', 'nurse'], methods=['GET'])
@login_required
def get_patient_nursenotes(pid):
    """
    Retrieves the all nursenote object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    notes = [notes.to_dict() for notes in patient.nursenotes]
    return jsonify(notes)


@api_views.route('/patients/<int:pid>/nursenotes/<notes_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/nursenotes/get_nursenote.yml')
@RBAC.allow(['doctor', 'nurse'], methods=['GET'])
@login_required
def get_patient_nursenote(pid, notes_id):
    """
    Retrieves the a specific nursenote object for a patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    notes = storage.get('NurseNote', 'id', notes_id)
    if (not notes) or (notes.pid != pid):
        abort(404, description='No such nursenote')

    return jsonify(notes.to_dict())


@api_views.route('/patients/<int:pid>/nursenotes/<note_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/nursenotes/delete_nursenote.yml',
           methods=['DELETE'])
@RBAC.allow(['nurse'], methods=['DELETE'])
@login_required
def delete_nursenote(pid, note_id):
    """
    Deletes a NurseNote Object for a patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    note = storage.get('NurseNote', 'id', note_id)
    if (not note) or (note.pid != pid):
        abort(404, description='No such nursenote')

    if note.created_by != current_user.staff_id:
        abort(403)

    storage.delete(note)
    storage.save()

    return jsonify({}), 200


@api_views.route('/patients/<int:pid>/nursenotes',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/nursenotes/post_nursenote.yml', methods=['POST'])
@RBAC.allow(['nurse'], methods=['POST'])
@login_required
def post_nursenote(pid):
    """
    Creates a new nursenote for a specific consultation
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    if 'note' not in request.get_json():
        abort(400, description="No note")

    data = request.get_json()
    data['pid'] = pid
    data['created_by'] = current_user.staff_id
    instance = NurseNote(**data)
    instance.save()
    instance = storage.get('NurseNote', 'id', instance.id)
    return jsonify(instance.to_dict()), 201


@api_views.route('/patients/<int:pid>/nursenotes/<note_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/nursenotes/put_nursenote.yml', methods=['PUT'])
@RBAC.allow(['nurse'], methods=['PUT'])
@login_required
def put_nursenote(pid, note_id):
    """
    Updates a nursenote for a patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    note = storage.get('NurseNote', 'id', note_id)
    if not note:
        abort(404)

    if note.created_by != current_user.staff_id:
        abort(403)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(note, key, value)
    storage.save()
    note = storage.get('NurseNote', 'id', note_id)
    return jsonify(note.to_dict()), 200
