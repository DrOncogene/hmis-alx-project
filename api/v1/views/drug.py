#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Drugs """
from models.drug import Drug
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/patients/<pid>/consultations/<consultation_id>/drugs',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/get_drugs.yml')
def get_drugs(consultation_id):
    """ Retrieves the all drug object for a specific consultation """
    all_prescriptions = storage.all(Prescription).values()
    all_drugs = storage.all(Drug).values()
    list_drugs = []
    list_prescriptions = []
    for prescription in all_prescriptions:
        if prescription.consultation_id == consultation_id:
            list_prescriptions.append(prescription.drug_id)
    for drug in all_drugs:
        for drug_id in list_drugs:
            if drug.id == drug_id:
                list_drugs.append(drug.to_dict())
    return jsonify(list_drugs)

@app_views.route('/drugs', methods=['GET'], strict_slashes=False)
@swag_from('documentation/drugs/all_drugs.yml')
def get_drugs():
    """ Retrieves the list of all drug object or a specific drug """
    all_drugs = storage.all(Drug).values()
    list_drugs = []
    for drug in all_drugs:
        list_drugs.append(drug.to_dict())
    return jsonify(list_drugs)


@app_views.route('/drugs/<drug_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/drugs/get_drugs.yml', methods=['GET'])
def get_drug(drug_id):
    """ Retrieves an drug """
    drug = storage.get(Drug, drug_id)
    if not drug:
        abort(404)

    return jsonify(drug.to_dict())


@app_views.route('/drugs/<drug_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/drugs/delete_drug.yml', methods=['DELETE'])
def delete_drug(drug_id):
    """
    Deletes a drug Object
    """

    drug = storage.get(Drug, drug_id)
    
    if not drug:
        abort(404)

    storage.delete(drug)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/drugs', methods=['POST'], strict_slashes=False)
@swag_from('documentation/drugs/post_drug.yml', methods=['POST'])
def post_drug():
    """
    Creates a drug
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing drug name")
    if 'dose' not in request.get_json():
        abort(400, description="Missing drug")
    if 'unit' not in request.get_json():
        abort(400, description="Missing drug unit")
    if 'brand' not in request.get_json():
        abort(400, description="Missing drug brand")
    if 'formulation' not in request.get_json():
        abort(400, description="Missing drug formulation")
    if 'route' not in request.get_json():
        abort(400, description="Missing drug route")

    data = request.get_json()
    instance = Drug(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/drugs/<drug_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/drug/put_drug.yml', methods=['PUT'])
def put_drug(drug_id):
    """
    Updates a drug
    """
    drug = storage.get(Drug, drug_id)

    if not drug:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(drug, key, value)
    storage.save()
    return make_response(jsonify(drug.to_dict()), 200)
