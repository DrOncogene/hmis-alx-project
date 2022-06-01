#!/usr/bin/python3
""" objects that handle all default RestFul API actions for NurseNote """
from models.notes.nursenote import NurseNote
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/patients/<pid>/nursenotes',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/get_nursenotes.yml')
def get_nursenotes(pid):
    """ Retrieves the all nursenote object for a specific patient """
    all_nursenotes = storage.all(NurseNote).values()
    list_nursenotes = []
    for nursenote in all_nursenotes:
        if nursenote.pid == pid:
            list_nursenotes.append(nursenote.to_dict())
    return jsonify(list_nursenotes)

@app_views.route('/patients/<pid>/consultations/<consultation_id>/nursenotes',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/get_nursenote.yml')
def get_nursenotes(consultation_id):
    """ Retrieves the all nursenote object for a specific consultation """
    all_nursenotes = storage.all(NurseNote).values()
    list_nursenotes = []
    for nursenote in all_nursenotes:
        if nursenote.consultation_id == consultation_id:
            list_nursenotes.append(nursenote.to_dict())
    return jsonify(list_nursenotes)

@app_views.route('/patients/<pid>/consultations/<consultation_id>/nursenotes/<nursenote_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultations/consultation_id/nursenotes/get_nursenote.yml')
def get_nursenote(nursenote_id):
    """ Retrieves the a specific nursenote object for a specific consultation """
    nursenote = storage.get(NurseNote, nursenote_id)
    if not nursenote:
        abort(404)

    return jsonify(nursenote.to_dict())

@app_views.route('/patients/<pid>/consultations/<consultation_id>/nursenotes/<nursenote_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultations/consultation_id>/nursenotes/delete_nursenote.yml',
           methods=['DELETE'])

def delete_nursenote(nursenote_id):
    """
    Deletes a NurseNote Object for a specific consultation
    """

    nursenote = storage.get(NurseNote, nursenote_id)
    
    if not nursenote:
        abort(404)

    storage.delete(nursenote)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<pid>/consultations/<consultation_id>/nursenotes',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/post_nursenote.yml', methods=['POST'])
def post_nursenote(pid, consultation_id):
    """
    Creates a new nursenote for a specific consultation
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    pid = pid
    consultation_id = consultation_id
    if 'note' not in request.get_json():
        abort(400, description="No note")

    data = request.get_json()
    instance = NurseNote(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/patients/<pid>/consultations/<consultation_id>/nursenotes/<nursenote_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/nursenotes/put_nursenote.yml',
           methods=['PUT'])
def put_nursenote(nursenote_id):
    """
    Updates a nursenote for a specific consultation
    """
    nursenote = storage.get(NurseNote, nursenote_id)

    if not nursenote:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(nursenote, key, value)
    storage.save()
    return make_response(jsonify(nursenote.to_dict()), 200)
