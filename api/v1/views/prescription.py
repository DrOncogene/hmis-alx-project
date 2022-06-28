#!/usr/bin/python3
"""
objects that handle all default RestFul API actions for Prescriptions
"""
from flasgger.utils import swag_from
from flask import abort, jsonify, make_response, request

from api.v1.views import app_views
from models.notes.prescription import Prescription, DrugPrescription
from storage import storage


@app_views.route('/patients/<int:pid>/prescriptions',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/get_prescriptions.yml')
def get_patient_prescriptions(pid):
    """
    Retrieves the all prescription object for a specific patient
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    prescriptions = [[drug.to_dict() for drug in presc.drugs]
                     for presc in patient.prescriptions]
    
    return jsonify(prescriptions)


@app_views.route('/patients/<int:pid>/consultations/<consultation_id>/prescription',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/get_prescription.yml')
def get_consult_prescriptions(pid, consultation_id):
    """
    Retrieves the prescription object for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consultation_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    prescriptions = [drug.to_dict() for drug in consultation.prescription.drugs]
    return jsonify(prescriptions)


@app_views.route('/patients/<int:pid>/consultations/<consult_id>/prescriptions/<presc_id>/drugs/drugpresc_id',
                 methods=['POST'], strict_slashes=False)
@app_views.route('/patients/<int:pid>/consultations/<consult_id>/prescriptions/<prescription_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/consultations/consultation_id>/prescriptions/delete_prescription.yml',
           methods=['DELETE'])
def delete_prescription(pid, consult_id, prescription_id, drugpresc_id=None):
    """
    Deletes a Prescription Object for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consult_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    if drugpresc_id is not None:
        prescription = storage.get('DrugPrescription', 'id', drugpresc_id)
    else:
        prescription = storage.get('Prescription', 'id', prescription_id)

    if not prescription:
        abort(404, description='No such prescription')

    storage.delete(prescription)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients/<int:pid>/consultations/<consult_id>/prescriptions/<presc_id>/drugs',
                 methods=['POST'], strict_slashes=False)
@app_views.route('/patients/<int:pid>/consultations/<consult_id>/prescriptions',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patient/patient_id/consultations/consultation_id/post_prescription.yml', methods=['POST'])
def post_prescription(pid, consult_id, presc_id=None):
    """
    Creates a new prescription for a specific consultation
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consult_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    if presc_id is not None:
        if 'drug_id' not in request.get_json():
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
        data['pid'] = pid
        data['consultation_id'] = consult_id
        data['prescription_id'] = presc_id
        instance = DrugPrescription(**data)
        instance.save()
        instance = storage.get('DrugPrescription', 'id', instance.id)
        return make_response(jsonify(instance.to_dict()), 201)

    presc = Prescription(pid=pid, consultation_id=consult_id)
    presc.save()
    presc = storage.get('Prescription', 'id', presc.id)
    return make_response(jsonify(presc.to_dict()), 201)


# @app_views.route('/patients/<pid>/consultations/<consultation_id>/prescriptions/<prescription_id>', methods=['PUT'],
#                  strict_slashes=False)
# @swag_from('documentation/patient/patient_id/consultations/consultation_id/prescriptions/put_prescription.yml',
#            methods=['PUT'])
# def put_prescription(pid, consult_id, presc_id=None):
#     """
#     Updates a prescription for a specific consultation
#     """
#     if not request.get_json():
#         abort(400, description="Not a JSON")

#     patient = storage.get('Patient', 'pid', pid)
#     if not patient:
#         abort(404, description="Patient not found")

#     consultation = storage.get('Consultation', 'id', consult_id)
#     if (not consultation) or (consultation.pid != pid):
#         abort(404, description="Consultation not found")

#     ignore = ['id', 'pid', 'consultation_id', 'created_at', 'created_by']

#     data = request.get_json()
#     for key, value in data.items():
#         if key not in ignore:
#             setattr(prescription, key, value)
#     storage.save()
#     return make_response(jsonify(prescription.to_dict()), 200)
