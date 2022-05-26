#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Prescriptions """
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from storage import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/staffs', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Doctor, Nurse, Pharmacist, RecordOfficer, Admin]
    names = ["doctor", "nurse", "pharmacist", "recordofficer", "admin"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)

@app_views.route('/staffs/<job_title>', methods=['GET'], strict_slashes=False)
def number_objects(job_title):
    """ Retrieves the number of a specific objects by type """
    titles = {
            "admin": Admin,
            "doctor": Doctor,
            "nurse": Nurse,
            "pharmacist": Pharmacist,
            "recordOfficer": RecordOfficer
    }

    if not job_title in titles:
        abort(404)

    num_objs = {}
    num_objs[job_title] = storage.count(titles[job_title])

    return jsonify(num_objs)

@app_views.route('/staff/<job_title>/<staff_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/staff/<job_title>/get_staff.yml', methods=['GET'])
def get_staff(job_title, staff_id):
    """ Retrieves an staff """

    titles = {
            "admin": Admin,
            "doctor": Doctor,
            "nurse": Nurse,
            "pharmacist": Pharmacist,
            "recordOfficer": RecordOfficer
    }
    staff = storage.get(titles[job_title], staff_id)
    if not staff:
        abort(404)

    return jsonify(staff.to_dict())

@app_views.route('/staff/<job_title>/<staff_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/staff/<job_title>/delete_staff.yml', methods=['DELETE'])
def delete_staff(job_title, staff_id):
    """
    Deletes a staff Object
    """

    titles = {
            "admin": Admin,
            "doctor": Doctor,
            "nurse": Nurse,
            "pharmacist": Pharmacist,
            "recordOfficer": RecordOfficer
    }

    staff = storage.get(titles[job_title], staff_id)
    if not staff:
        abort(404)

    storage.delete(doctor)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/staff/<job_title>', methods=['POST'], strict_slashes=False)
@swag_from('documentation/staff/job_title/post_staff.yml', methods=['POST'])
def post_staff(job_title):
    """
    Creates a staff
    """
    if not request.get_json():
        abort(400, description="Not a JSON")


    titles = {
            "admin": Admin,
            "doctor": Doctor,
            "nurse": Nurse,
            "pharmacist": Pharmacist,
            "recordOfficer": RecordOfficer
    }
    if 'first_name' not in request.get_json():
        abort(400, description="Missing first name")
    if 'last_name' not in request.get_json():
        abort(400, description="Missing last name")
    if 'gender' not in request.get_json():
        abort(400, description="Missing gender")
    if 'dob' not in request.get_json():
        abort(400, description="Missing date of birth")
    if 'address' not in request.get_json():
        abort(400, description="Missing address")
    if 'kinfirst_name' not in request.get_json():
        abort(400, description="Missing next of kin first name")
    if 'kinlast_name' not in request.get_json():
        abort(400, description="Missing next of kin last name")
    if 'kintelephone_number' not in request.get_json():
        abort(400, description="Missing next of kin contact address")

    data = request.get_json()
    instance = titles[job_title](**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/staff/<job_title>/<staff_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/staff/staff_id/put_staff.yml', methods=['PUT'])
def put_staff(job_title, staff_id):
    """
    Updates a staff
    """
    if not request.get_json():
        abort(400, description="Not a JSON")


    titles = {
            "admin": Admin,
            "doctor": Doctor,
            "nurse": Nurse,
            "pharmacist": Pharmacist,
            "recordOfficer": RecordOfficer
    }

    staff = storage.get(titles[job_title], staff_id)

    if not staff:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'job_title', 'staff_id', 'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(titles[job_title], key, value)
    storage.save()
    return make_response(jsonify(titles[job_title].to_dict()), 200)
