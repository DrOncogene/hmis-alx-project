#!/usr/bin/python3
"""generates sample data for the database"""
from sys import argv
from random import randint, uniform
from datetime import date, datetime, timedelta
import sys

from models.patient import Patient
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from models.notes.consult import Consultation
from models.notes.prescription import Prescription, DrugPrescription
from models.notes.vitals import VitalSign
from models.notes.nursenote import NurseNote
from models.drug import Drug
from storage import storage

staff_cls = [Doctor, Nurse, Pharmacist, RecordOfficer]
NUM_STAFFS = 0
sex = ('Male', 'Female')
marital_status = ('Single', 'Married', 'Widowed', 'Divorced')
consults = []
drugs = []
routes = ('Oral', 'Intravenous', 'Intramuscular')
freqs = ('daily', 'bd', 'tds', 'qds', 'nocte', 'PRN')


def random_phone():
    ph_no = []
    ph_no.append(str(randint(6, 9)))
    for i in range(1, 10):
        ph_no.append(str(randint(0, 9)))
    return ''.join(ph_no)

def generate_staffs(cls: type, n: int):
    cls_name = cls.__name__
    for i in range(1, n + 1):
        new = cls()
        new.first_name = new.last_name = f'{cls_name}{i}'
        new.gender = sex[randint(0, 1)]
        new.marital_status = marital_status[randint(0, 3)]
        year = randint(1990, 2022)
        month = randint(1, 12)
        day = randint(1, 28)
        new.dob = date.fromisoformat(f'{year}-{month:02}-{day:02}')
        new.address = f'{randint(1, 20)}, Nowhere, New Jersey'
        new.phone_number = random_phone()
        new.next_of_kin = f'kin{i}'
        new.kin_address = new.address
        new.username = f'{cls_name}{i}'
        new.email = f'{cls_name}{i}@hmis.com'
        new.set_password(f'password{i}')
        new.save()

def generate_patients(n: int):
    for i in range(n):
        email = f'RecordOfficer{randint(1, NUM_STAFFS)}@hmis.com'
        record_officer = storage.get(RecordOfficer, 'email', email)
        new = Patient(created_by=record_officer.staff_id)
        new.first_name = new.last_name = f'Patient{i}'
        new.gender = sex[randint(0, 1)]
        new.marital_status = marital_status[randint(0, 3)]
        year = randint(1990, 2022)
        month = randint(1, 12)
        day = randint(1, 28)
        new.dob = date.fromisoformat(f'{year}-{month:02}-{day:02}')
        new.address = f'{randint(10, 20)}, Nowhere, Patient Lane'
        new.phone_number = random_phone()
        new.next_of_kin = f'kin{i}'
        new.kin_address = new.address
        new.email = f'patient{i}@hmispat.com'
        new.save()

def generate_consults(n: int):
    for i in range(n):
        pat_email = f'patient{randint(0, n - 1)}@hmispat.com'
        patient = storage.get(Patient, 'email', pat_email)
        doc_email = f'Doctor{randint(1, NUM_STAFFS)}@hmis.com'
        doc = storage.get(Doctor, 'email', doc_email)
        new = Consultation(created_by=doc.staff_id)
        consults.append(new.id)
        new.pid = patient.pid
        new.pc = f'Complaint{i}'
        new.hpc = f'History{i}'
        new.plan = f'Plan{i}'
        new.prov_diag = f'Disease{i}'
        new.save()

def generate_drugs(n: int):
    for i in range(n):
        pharm_email = f'Pharmacist{randint(1, NUM_STAFFS)}@hmis.com'
        pharm = storage.get(Pharmacist, 'email', pharm_email)
        new = Drug(created_by=pharm.staff_id)
        new.name = f'Drug{i}'
        new.dose = f'{5 * i}mg'
        new.route = routes[randint(0, 2)]
        new.brand = f'Brand{i}'
        new.stock_date = datetime.now()
        new.expiry_date = new.stock_date + timedelta(weeks=55)
        drugs.append(new.id)
        new.save()

def generate_prescriptions(n: int):
    for i in range(n):
        pat_email = f'patient{randint(0, n - 1)}@hmispat.com'
        patient = storage.get(Patient, 'email', pat_email)
        pharm_email = f'Pharmacist{randint(1, NUM_STAFFS)}@hmis.com'
        pharm = storage.get(Pharmacist, 'email', pharm_email)
        doc_email = f'Doctor{randint(1, NUM_STAFFS)}@hmis.com'
        doc = storage.get(Doctor, 'email', doc_email)
        new = Prescription(created_by=doc.staff_id)
        drug = storage.get(Drug, 'id', drugs[randint(0, n - 1)])
        drug_presc = DrugPrescription(drug_id=drug.id)
        drug_presc.prescription = new
        drug_presc.dose = drug.dose
        drug_presc.frequency = freqs[randint(0, 5)]
        drug_presc.duration = f'{randint(5, 14)} days'
        drug_presc.route = drug.route
        drug = storage.get(Drug, 'id', drugs[randint(0, n - 1)])
        drug_presc = DrugPrescription(drug_id=drug.id)
        drug_presc.drug_id = drug.id
        drug_presc.prescription = new
        drug_presc.dose = drug.dose
        drug_presc.frequency = freqs[randint(0, 5)]
        drug_presc.duration = f'{randint(5, 14)} days'
        drug_presc.route = drug.route
        new.pid = patient.pid
        new.dispensed_by = pharm.staff_id
        new.consultation_id = consults[i]
        new.save()

def gen_nursenotes(n: int):
    for i in range(n):
        nurse_email = f'Nurse{randint(1, NUM_STAFFS)}@hmis.com'
        nurse = storage.get(Nurse, 'email', nurse_email)
        pat_email = f'patient{randint(0, n - 1)}@hmispat.com'
        patient = storage.get(Patient, 'email', pat_email)
        new = NurseNote(created_by=nurse.staff_id)
        new.pid = patient.pid
        new.note = f'Documentation by Nurse{i}'
        new.save()

def generate_vitals(n: int):
    for i in range(n):
        nurse_email = f'Nurse{randint(1, NUM_STAFFS)}@hmis.com'
        nurse = storage.get(Nurse, 'email', nurse_email)
        new = VitalSign(created_by=nurse.staff_id)
        patient = storage.get(Patient, 'email', f'patient{randint(0, n - 1)}@hmispat.com')
        link_to_consult = randint(0, 1)
        if link_to_consult > 0:
            consult = storage.get('Consultation', 'id', consults[i])
            new.pid = consult.pid
            new.consultation_id = consult.id
        else:
            new.pid = patient.pid
        new.pr = randint(60, 100)
        new.rr = randint(12, 28)
        new.sbp = randint(100, 139)
        new.dbp = randint(60, 89)
        new.temp = round(uniform(36.5, 37.5), 1)
        new.spo2 = randint(80, 99)
        new.height = round(uniform(1.5, 2.0), 1)
        new.weight = round(uniform(45.0, 80.0), 1)
        new.save()

if __name__ == "__main__":
    try:
        num = int(argv[1])
    except (ValueError, IndexError) as err:
        print(f'Usage: ./datagenerator.py <num_of_entries>: {err}')
        sys.exit(1)

    NUM_STAFFS = num//5
    for i, cls in enumerate(staff_cls):
        generate_staffs(cls, NUM_STAFFS)

    generate_patients(num)
    generate_consults(num)
    generate_drugs(num)
    generate_prescriptions(num)
    gen_nursenotes(num)
    generate_vitals(num)
