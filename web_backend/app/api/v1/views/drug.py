#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Drugs """
from flasgger.utils import swag_from
from flask import abort, jsonify, request
from flask_login import login_required, current_user

from models.drug import Drug
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/drugs', methods=['GET'], strict_slashes=False)
@swag_from('documentation/consultations/consultation_id/get_drugs.yml')
@RBAC.allow(['doctor', 'pharmacist'], methods=['GET'])
@login_required
def get_consult_drugs():
    """ Retrieves the all drug object for a specific consultation """
    drugs = [drug.to_dict() for drug in storage.all(Drug)]

    return jsonify(drugs)


@api_views.route('/drugs/<string:drug_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/drugs/get_drugs.yml', methods=['GET'])
@RBAC.allow(['doctor', 'pharmacist'], methods=['GET'])
@login_required
def get_drug(drug_id):
    """ Retrieves an drug """
    drug = storage.get(Drug, 'id', drug_id)
    if not drug:
        abort(404, description="drug not found")

    return jsonify(drug.to_dict())


@api_views.route('/drugs/<drug_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/drugs/delete_drug.yml', methods=['DELETE'])
@RBAC.allow(['pharmacist'], methods=['DELETE'])
@login_required
def delete_drug(drug_id):
    """
    Deletes a drug Object
    """
    drug = storage.get(Drug, 'id', drug_id)
    if not drug:
        abort(404, description="drug not found")

    storage.delete(drug)
    storage.save()

    return jsonify({})


@api_views.route('/drugs', methods=['POST'], strict_slashes=False)
@swag_from('documentation/drugs/post_drug.yml', methods=['POST'])
@RBAC.allow(['pharmacist'], methods=['POST'])
@login_required
def post_drug():
    """
    Creates a drug
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing drug name")
    if 'dose' not in request.get_json():
        abort(400, description="Missing drug dose")
    if 'brand' not in request.get_json():
        abort(400, description="Missing drug brand")
    if 'formulation' not in request.get_json():
        abort(400, description="Missing drug formulation")
    if 'route' not in request.get_json():
        abort(400, description="Missing drug route")

    data = request.get_json()
    data['created_by'] = current_user.staff_id
    instance = Drug(**data)
    instance.save()
    return jsonify(instance.to_dict()), 201


@api_views.route('/drugs/<drug_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/drug/put_drug.yml', methods=['PUT'])
@RBAC.allow(['pharmacist'], methods=['PUT'])
@login_required
def put_drug(drug_id):
    """
    Updates a drug
    """
    drug = storage.get(Drug, 'id', drug_id)
    if not drug:
        abort(404, description="drug not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(drug, key, value)
    drug.updated_by = current_user.staff_id
    storage.save()
    return jsonify(drug.to_dict())
