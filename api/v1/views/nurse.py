#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Nurses """
from flask import jsonify, abort
from flasgger.utils import swag_from

from models.notes.nurse import Nurse
from storage import storage
from api.v1.views import app_views


@app_views.route('/staffs/nurses/<string:staff_id>/vitals',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/nurses/staff_id/get_vitals.yml')
def get_vitals(staff_id):
    """ Retrieves the list of a nurses vitals sign record """
    
    staff_id = int(staff_id[3:])
    nurse = storage.get(Nurse, 'staff_id', staff_id)
    if not nurse:
        abort(404, description="Staff does not exist")

    nurse_vitals = [vitals.to_dict() for vitals in nurse.vitals]
    
    return jsonify(nurse_vitals)


@app_views.route('/staffs/nurses/<string:staff_id>/nursenotes',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/nurses/staff_id/get_nursenotes.yml')
def get_nursenotes(staff_id):
    """ Retrieves the list of a nurses nursenotes """
    staff_id = int(staff_id[3:])
    nurse = storage.get(Nurse, 'staff_id', staff_id)
    
    if not nurse:
        abort(404, description="Staff does not exist")

    nursenotes = [note.to_dict() for note in nurse.nursenotes]
    
    return jsonify(nursenotes)
