#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Nurses """
from models.notes.vitals import VitalSign
from models.notes.nursenote import NurseNote
from storage import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/staffs/nurse/<staff_id>/vitals', methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/nurse/staff_id/get_vitals.yml')
def get_vitals(staff_id):
    """ Retrieves the list of a nurses vitals sign record """
    all_vitals = storage.all(VitalSign).values()
    nurse_vitals = []
    for vitals in all_vitals:
        if vitals.created_by == staff_id:
            nurse_vitals.append(vitals.to_dict())
    return jsonify(nurse_vitals)


@app_views.route('/staffs/nurse/<staff_id>/nursenotes', methods=['GET'], strict_slashes=False)
@swag_from('documentation/staffs/nurse/staff_id/get_nursenotes.yml')
def get_nursenotes(staff_id):
    """ Retrieves the list of a nurses nursenotes """
    all_nursenotes = storage.all(NurseNote).values()
    nurse_nursenotes = []
    for nursenotes in all_nursenotes:
        if nursenotes.created_by == staff_id:
            nurse_nursenotes.append(nursenotes.to_dict())
    return jsonify(nurse_nursenotes)
