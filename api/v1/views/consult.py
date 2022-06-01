#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Consultations """
from models.notes.consult import Consultation
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/patients/<pid>/consultations', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/get_consultations.yml')
def get_consultations(pid):
    """ Retrieves the all consultation object for a specific patient """
    all_consultations = storage.all(Consulation).values()
    list_consultations = []
    for consultation in all_consultations:
        if consulation.pid == pid:
            list_consultations.append(consultation.to_dict())
    return jsonify(list_consultations)


@app_views.route('/patients/<pid>/consultations/<consultation_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/get_consultation.yml')
def get_consultation(consulation_id):
    """ Retrieves the a specific consultation object for a specific patient """
    consultation = storage.get(Consultation, consultation_id)
    if not consultation:
        abort(404)

    return jsonify(consultation.to_dict())

@app_views.route('/patients/<pid>/consutations/<consultation_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/delete_consulation.yml',
           methods=['DELETE'])

def delete_consulation(consulation_id):
    """
    Deletes a Consulation Object for a specific patient
    """

    consultation = storage.get(Consultation, consultation_id)
    
    if not consulation:
        abort(404)

    storage.delete(consulation)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<pid>/consultations', methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/post_consultation.yml', methods=['POST'])
def post_consultation(pid):
    """
    Creates a new consultation for a specific patient
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    pid = pid
    if 'pc' not in request.get_json():
        abort(400, description="Missing presenting complaints")
    if 'hpc' not in request.get_json():
        abort(400, description="Missing history")
    if 'prov_diag' not in request.get_json():
        abort(400, description="Missing diagnosis")
    if 'plan' not in request.get_json():
        abort(400, description="Missing plan")

    data = request.get_json()
    instance = Consulation(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/patients/<pid>/consultations/<consultation_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/put_consultation.yml', methods=['PUT'])
def put_consultation(consulation_id):
    """
    Updates a consultation for a specific patient
    """
    consultation = storage.get(Consultation, consultation_id)

    if not consultation:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(consultation, key, value)
    storage.save()
    return make_response(jsonify(consultation.to_dict()), 200)
