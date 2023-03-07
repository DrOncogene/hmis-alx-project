#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Prescriptions """
from datetime import datetime

from flask import jsonify, abort, request
from flasgger.utils import swag_from
from flask_login import current_user, login_required

from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/staffs', methods=['GET'], strict_slashes=False)
@login_required
def staff_count():
    """ Retrieves the number of each objects by type """
    classes = [Doctor, Nurse, Pharmacist, RecordOfficer, Admin]
    names = ["doctor", "nurse", "pharmacist", "recordofficer", "admin"]

    num_objs = {}
    for i, cls in enumerate(classes):
        num_objs[names[i]] = storage.count(cls)

    return jsonify(num_objs)


@api_views.route('/staffs/<string:job_title>',
                 methods=['GET'], strict_slashes=False)
@login_required
def staff_by_type(job_title: str):
    """ Retrieves the number of a specific objects by type """
    titles = {
        "admins": Admin,
        "doctors": Doctor,
        "nurses": Nurse,
        "pharmacists": Pharmacist,
        "recordofficers": RecordOfficer
    }

    if job_title not in titles:
        abort(404, description=f"{job_title} is not valid job title")

    staffs = storage.all(titles[job_title])
    staffs_of_type = [staff.to_dict() for staff in staffs]

    return jsonify(staffs_of_type)


@api_views.route('/staffs/<string:job_title>/<string:staff_id>',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staff/<job_title>/get_staff.yml', methods=['GET'])
@RBAC.allow(['admin'], methods=['GET'])
@login_required
def get_staff(job_title, staff_id):
    """ Retrieves a staff """
    titles = {
        "admins": Admin,
        "doctors": Doctor,
        "nurses": Nurse,
        "pharmacists": Pharmacist,
        "recordofficers": RecordOfficer
    }

    staff_id = int(staff_id[3:])
    staff = storage.get(titles[job_title], 'staff_id', staff_id)
    if not staff:
        abort(404, description="staff not found")

    return jsonify(staff.to_dict())


@api_views.route('/staffs/<string:job_title>/<string:staff_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/staff/<job_title>/delete_staff.yml',
           methods=['DELETE'])
@RBAC.allow(['admin'], methods=['DELETE'])
@login_required
def delete_staff(job_title, staff_id):
    """
    Deletes a staff Object
    """

    titles = {
        "admins": Admin,
        "doctors": Doctor,
        "nurses": Nurse,
        "pharmacists": Pharmacist,
        "recordOfficers": RecordOfficer
    }

    staff_id = int(staff_id[3:])
    staff = storage.get(titles[job_title], 'staff_id', staff_id)
    if not staff:
        abort(404, description="staff not found")

    staff.delete()
    storage.save()

    return jsonify({})


@api_views.route('/staffs/<string:job_title>', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/staffs/<job_title>/create_staff.yml',
           methods=['POST'])
@RBAC.allow(['admin'], methods=['POST'])
@login_required
def create_staff(job_title):
    """
    Creates a staff
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    titles: dict = {
        "admins": Admin,
        "doctors": Doctor,
        "nurses": Nurse,
        "pharmacists": Pharmacist,
        "recordOfficers": RecordOfficer
    }

    if 'username' not in request.get_json():
        abort(400, description="Missing username")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    if 'first_name' not in request.get_json():
        abort(400, description="Missing first name")
    if 'last_name' not in request.get_json():
        abort(400, description="Missing last name")
    if 'gender' not in request.get_json():
        abort(400, description="Missing gender")
    if 'email' not in request.get_json():
        abort(400, description="Missing email address")
    if 'dob' not in request.get_json():
        abort(400, description="Missing date of birth")
    if 'marital_status' not in request.get_json():
        abort(400, description="Missing marital status")
    if 'address' not in request.get_json():
        abort(400, description="Missing address")
    if 'phone_number' not in request.get_json():
        abort(400, description="Missing phone number")
    if 'next_of_kin' not in request.get_json():
        abort(400, description="Missing next of kin")
    if 'kin_address' not in request.get_json():
        abort(400, description="Missing next of kin address")

    data: dict = request.get_json()
    data['dob'] = datetime.strptime(data['dob'], '%d/%m/%Y')
    data['created_by'] = current_user.staff_id
    password = data.pop('password')
    data.pop('role', None)
    staff = titles[job_title](**data)
    staff.set_password(password)

    storage.save()

    return jsonify(staff.to_dict()), 201

@api_views.route('/staffs/<string:job_title>/<string:staff_id>',
                 methods=['PUT'], strict_slashes=False)
@swag_from('documentation/staff/staff_id/put_staff.yml', methods=['PUT'])
@RBAC.allow(['admin'], methods=['PUT'])
def put_staff(job_title, staff_id):
    """
    Updates a staff
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    titles: dict = {
        "admins": Admin,
        "doctors": Doctor,
        "nurses": Nurse,
        "pharmacists": Pharmacist,
        "recordOfficers": RecordOfficer
    }

    staff_id = int(staff_id[3:])
    staff = storage.get(titles[job_title], 'staff_id', staff_id)

    if not staff:
        abort(404, description="Staff does not exist")

    ignore = ['id', 'job_title', 'staff_id', 'created_at', 'created_by', 'role']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore and hasattr(staff, key):
            setattr(staff, key, value)
    staff.updated_by = current_user.staff_id
    storage.save()

    return jsonify(staff.to_dict()), 200
