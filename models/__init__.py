#!usr/bin/python3
from storage import storage

staff_ids = []
hospital_numbers = []

staffs = storage.all('Staff')
patients = storage.all('Patients')

staff_ids = sorted([staff.staff_id for staff in staffs.values()])
hospital_numbers = sorted([patient.hosp_num for patient in patients.values()])
