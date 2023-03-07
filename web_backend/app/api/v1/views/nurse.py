#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Nurses """
from flask import jsonify, abort
from flasgger.utils import swag_from
from flask_login import login_required

from models.nurse import Nurse
from storage import storage
from web_backend.app.roles import RBAC
from .import api_views


@api_views.route('/staffs/nurses/<string:staff_id>/vitals',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/nurses/staff_id/get_vitals.yml')
@RBAC.allow(['nurse'], methods=['GET'])
@login_required
def get_nurse_vitals(staff_id):
    """ Retrieves the list of a nurses vitals sign record """

    staff_id = int(staff_id[3:])
    nurse = storage.get(Nurse, 'staff_id', staff_id)
    if not nurse:
        abort(404, description="Staff does not exist")

    nurse_vitals = [vitals.to_dict() for vitals in nurse.vitals]
    return jsonify(nurse_vitals)


@api_views.route('/staffs/nurses/<string:staff_id>/notes',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/nurses/staff_id/get_nursenotes.yml')
@RBAC.allow(['nurse'], methods=['GET'])
@login_required
def get_nurse_nursenotes(staff_id):
    """ Retrieves the list of a nurses nursenotes """

    staff_id = int(staff_id[3:])
    nurse = storage.get(Nurse, 'staff_id', staff_id)
    if not nurse:
        abort(404, description="Staff does not exist")

    nursenotes = [note.to_dict() for note in nurse.nursenotes]
    return jsonify(nursenotes)
