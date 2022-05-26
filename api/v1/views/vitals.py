#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Vital Signs """
from models.notes.vitals import VitalSign
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

#the get request for consultation has the ids for vitals, i believe this is redundant
@app_views.route('/patients/<pid>/<consultation_id>/<vitals_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/get_vitals.yml')
def get_vitals(vitals_id):
    """ Retrieves the a specific vitals object for a specific consultation """
    vitals = storage.get(VitalSign, vitals_id)
    if not vitals:
        abort(404)

    return jsonify(vitals.to_dict())

@app_views.route('/patients/<pid>/<consultation_id>/<vitals_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/delete_vitals.yml',
           methods=['DELETE'])

def delete_vitals(vitals_id):
    """
    Deletes a VitalSign Object for a specific consultation
    """

    vitals = storage.get(VitalSign, vitals_id)
    
    if not vitals:
        abort(404)

    storage.delete(vitals)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<pid>/<consultation_id>',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/post_vitals.yml', methods=['POST'])
def post_vitals(pid, consulation_id):
    """
    Creates a new vitals for a specific consultation
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    pid = pid
    consulation_id = consulation_id
    if 'pr' not in request.get_json():
        abort(400, description="Missing pulse rate")
    if 'rr' not in request.get_json():
        abort(400, description="Missing respiratory rate")
    if 'bp' not in request.get_json():
        abort(400, description="Missing blood pressure")
    if 'temp' not in request.get_json():
        abort(400, description="Missing temperature")
    if 'spo2' not in request.get_json():
        abort(400, description="Missing oxygen saturation")
    if 'height' not in request.get_json():
        abort(400, description="Missing height")
    if 'weight' not in request.get_json():
        abort(400, description="Missing weight")

    data = request.get_json()
    instance = VitalSign(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/patients/<pid>/<consultation_id>/<vitals_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/put_vitals.yml',
           methods=['PUT'])
def put_vitals(vitals_id):
    """
    Updates a vitals for a specific consultation
    """
    vitals = storage.get(VitalSign, vitals_id)

    if not vitals:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(vitals, key, value)
    storage.save()
    return make_response(jsonify(vitals.to_dict()), 200)
