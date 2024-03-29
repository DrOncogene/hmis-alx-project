#!/usr/bin/python3
"""
objects that handle all default RestFul API actions for Prescriptions
"""
from flasgger.utils import swag_from
from flask import abort, jsonify, request
from flask_login import current_user, login_required

from models.notes.prescription import Prescription, DrugPrescription
from storage import storage
from web_backend.app.roles import RBAC
from . import api_views


@api_views.route('/patients/<int:pid>/prescriptions',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/patients/patient_id/get_prescriptions.yml')
@RBAC.allow(['doctor', 'nurse', 'pharmacist'], methods=['GET'])
@login_required
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


@api_views.route('/patients/<int:pid>/consultations/<consult_id>/prescription',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/prescriptions/get_prescription.yml')
@RBAC.allow(['doctor', 'nurse', 'pharmacist'], methods=['GET'])
@login_required
def get_consult_prescriptions(pid, consult_id):
    """
    Retrieves the prescription object for a specific consultation
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consult = storage.get('Consultation', 'id', consult_id)
    if (not consult) or (consult.pid != pid):
        abort(404, description="Consultation not found")

    prescription = consult.prescription
    if not prescription:
        abort(404, description="No prescriptions for this consultation")
    prescription = [drug.to_dict() for drug in prescription.drugs]

    return jsonify(prescription)


@api_views.route(('/patients/<int:pid>/consultations/<consult_id>/'
                  'prescription/drugs/<drugpresc_id>'),
                 methods=['DELETE'], strict_slashes=False)
@api_views.route('/patients/<int:pid>/consultations/<consult_id>/prescription',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/patients/prescriptions/delete_prescription.yml',
           methods=['DELETE'])
@RBAC.allow(['doctor'], methods=['DELETE'])
@login_required
def delete_prescription(pid, consult_id, drugpresc_id=None):
    """
    Deletes the prescription for a consultation
    or a drug from a prescription
    """
    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consult_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    if drugpresc_id is not None:
        drug_presc = storage.get('DrugPrescription', 'id', drugpresc_id)
        presc = consultation.prescription
        if not (drug_presc or (drug_presc in presc.drugs)):
            abort(404, description="No such drug prescription")
        prescription = drug_presc
    else:
        prescription = consultation.prescription

    if not prescription:
        abort(404, description='No such prescription')

    if prescription.created_by != current_user.staff_id:
        abort(403)

    storage.delete(prescription)
    storage.save()

    return jsonify({})


@api_views.route(('/patients/<int:pid>/consultations/'
                  '<consult_id>/prescription/drugs'), methods=['POST'],
                 defaults={'drugs': 'drugs'}, strict_slashes=False)
@api_views.route('/patients/<int:pid>/consultations/<consult_id>/prescription',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/patients/prescriptions/post_prescription.yml',
           methods=['POST'])
@RBAC.allow(['doctor'], methods=['POST'])
@login_required
def post_prescription(pid, consult_id, drugs=None):
    """
    Creates a new prescription for a specific consultation
    or adds a new drug to an existing prescription
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consult_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    if drugs is not None:
        if 'drug_id' not in request.get_json():
            abort(400, description="Missing drug")
        if 'dose' not in request.get_json():
            abort(400, description="Missing dose")
        if 'frequency' not in request.get_json():
            abort(400, description="Missing dose frequency")
        if 'duration' not in request.get_json():
            abort(400, description="Missing dose duration")
        if 'route' not in request.get_json():
            abort(400, description="Missing drug route")

        data = request.get_json()
        data['pid'] = pid
        data['consultation_id'] = consult_id
        data['prescription_id'] = consultation.prescription.id
        data['created_by'] = current_user.staff_id
        instance = DrugPrescription(**data)
        instance.save()
        instance = storage.get('DrugPrescription', 'id', instance.id)
        return jsonify(instance.to_dict()), 201

    presc = Prescription(pid=pid, consultation_id=consult_id)
    presc.save()
    return jsonify(presc.to_dict()), 201


@api_views.route(('/patients/<int:pid>/consultations/'
                  '<consult_id>/prescription/drugs/<drugpresc_id>'),
                 methods=['PUT'], strict_slashes=False)
@swag_from('documentation/prescription/put_prescription.yml',
           methods=['PUT'])
@RBAC.allow(['doctor', 'pharmacist'], methods=['PUT'])
@login_required
def put_prescription(pid, consult_id, drugpresc_id):
    """
    Updates a prescription for a specific consultation
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    patient = storage.get('Patient', 'pid', pid)
    if not patient:
        abort(404, description="Patient not found")

    consultation = storage.get('Consultation', 'id', consult_id)
    if (not consultation) or (consultation.pid != pid):
        abort(404, description="Consultation not found")

    drug_presc = storage.get(DrugPrescription, 'id', drugpresc_id)
    presc = consultation.prescription
    if presc.created_by != current_user.staff_id:
        abort(403)

    if not (drug_presc or (drug_presc in presc.drugs)):
        abort(404, description="No such drug prescription")

    ignore = ['id', 'drug_id', 'pid', 'prescription_id',
              'created_at', 'created_by']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(drug_presc, key, value)
    storage.save()
    return jsonify(drug_presc.to_dict()), 200
