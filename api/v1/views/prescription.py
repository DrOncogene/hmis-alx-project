#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Prescriptions """
from models.notes.prescription import Prescription
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

#the get request for consultation has the ids for prescription, i believe this is redundant
@app_views.route('/patients/<pid>/<consultation_id>/<prescription_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/get_prescription.yml')
def get_prescription(prescription_id):
    """ Retrieves the a specific prescription object for a specific consultation """
    prescription = storage.get(Prescription, prescription_id)
    if not prescription:
        abort(404)

    return jsonify(prescription.to_dict())

@app_views.route('/patients/<pid>/<consultation_id>/<prescription_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/delete_prescription.yml',
           methods=['DELETE'])

def delete_prescription(prescription_id):
    """
    Deletes a Prescription Object for a specific consultation
    """

    prescription = storage.get(Prescription, prescription_id)
    
    if not prescription:
        abort(404)

    storage.delete(prescription)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<pid>/<consultation_id>',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/post_prescription.yml', methods=['POST'])
def post_prescription(pid, consulation_id):
    """
    Creates a new prescription for a specific consultation
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    pid = pid
    consulation_id = consulation_id
    if 'drug_name' not in request.get_json():
        abort(400, description="Missing drug")
    if 'dose' not in request.get_json():
        abort(400, description="Missing dose")
    if 'unit' not in request.get_json():
        abort(400, description="Missing dose unit")
    if 'frequency' not in request.get_json():
        abort(400, description="Missing dose frequency")
    if 'duration' not in request.get_json():
        abort(400, description="Missing dose duration")
    if 'route' not in request.get_json():
        abort(400, description="Missing drug route")

    data = request.get_json()
    instance = Prescription(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/patients/<pid>/<consultation_id>/<prescription_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultation_id/put_prescription.yml',
           methods=['PUT'])
def put_prescription(prescription_id):
    """
    Updates a prescription for a specific consultation
    """
    prescription = storage.get(Prescription, prescription_id)

    if not prescription:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(prescription, key, value)
    storage.save()
    return make_response(jsonify(prescription.to_dict()), 200)
