#!/usr/bin/python3
""" objects that handle all default RestFul API actions for NurseNote """
from flasgger.utils import swag_from
from flask import abort, jsonify, make_response, request

from api.v1.views import app_views
from models.notes.nursenote import NurseNote
from storage import storage


@app_views.route('/patients/<int:pid>/nursenotes',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/get_nursenotes.yml')
def get_patient_nursenotes(pid):
    """
    Retrieves the all nursenote object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    notes = [notes.to_dict() for notes in patient.nursenotes]
    return jsonify(notes)


# @app_views.route('/patients/<pid>/consultations/<consultation_id>/nursenotes',
#                  methods=['GET'], strict_slashes=False)
# @swag_from('documentation/patient/patient_id/consultations/consultation_id/get_nursenote.yml')
# def get_consult_nursenotes(consultation_id):
#     """ Retrieves the all nursenote object for a specific consultation """
#     all_nursenotes = storage.all(NurseNote).values()
#     list_nursenotes = []
#     for nursenote in all_nursenotes:
#         if nursenote.consultation_id == consultation_id:
#             list_nursenotes.append(nursenote.to_dict())
#     return jsonify(list_nursenotes)

@app_views.route('/patients/<int:pid>/nursenotes/<notes_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultations/consultation_id/nursenotes/get_nursenote.yml')
def get_nursenote(pid, notes_id):
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


@app_views.route('/patients/<int:pid>/nursenotes/<notes_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultations/consultation_id>/nursenotes/delete_nursenote.yml',
           methods=['DELETE'])
def delete_nursenote(pid, notes_id):
    """
    Deletes a NurseNote Object for a patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    notes = storage.get('NurseNote', 'id', notes_id)
    if (not notes) or (notes.pid != pid):
        abort(404, description='No such nursenote')

    storage.delete(notes)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<int:pid>/nursenotes',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/post_nursenote.yml', methods=['POST'])
def post_nursenote(pid, notes_id):
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
    instance = NurseNote(**data)
    instance.save()
    instance = storage.get('NurseNote', 'id', instance.id)
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/patients/<int:pid>/nursenotes/<notes_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/nursenotes/put_nursenote.yml',
           methods=['PUT'])
def put_nursenote(pid, notes_id):
    """
    Updates a nursenote for a patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    notes = storage.get('NurseNote', 'id', notes_id)
    if not notes:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(notes, key, value)
    storage.save()
    notes = storage.get('NurseNote', 'id', notes_id)
    return make_response(jsonify(notes.to_dict()), 200)
