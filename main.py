#!/usr/bin/python3
import os
import sys
import subprocess
from datetime import date
import re
import pprint
from models.patient import Patient
from models.staff import Staff
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from models.notes.consult import Consultation
from models.notes.prescription import Prescription
from models.notes.vitals import VitalSign
from models.notes.nursenote import NurseNote
from models.drug import Drug

current_user = None

try:
    os.remove('file.json')
except FileNotFoundError:
    pass

try:
    subprocess.run(['./empty_db.sh'], check=True)
    from storage import storage
except calledProcessError as err:
    print(err)

def get_option(prompt: str, choices: list):
    options = [str(option) for option in choices]
    choice = input(prompt).strip()
    while choice not in options:
        print(f'Invalid option ({choice}), try again')
        choice = input(prompt).strip()
    return int(choice)

def get_email():
    pattern = re.compile(r'\w+@\w+\.\w+')
    email = input('Enter your email: ')
    while (res := pattern.match(email)) is None:
        print('Invalid email')
        email = input('Enter your email: ')
    return res.string

def authenticate(username, password):
    user = storage.get(Staff, 'username', username)
    if user:
        if user.check_password(password):
            return user
        for i in range(3):
            print(f"Incorrect password, try again {3 - i} tries left")
            password = input('Enter your password: ')
    else:
        print('No with that username')
        

def logout():
    pass
def signup():
    print('WELCOME TO THE SIGNUP PAGE!\n')
    print('WHICH OF THE FOLLOWING ARE YOU?\n')
    print('1. Doctor\t2. Nurse\t3. Pharmacist\n')
    option = get_option('Choose option: ', [1, 2, 3])
    jobs = ['Doctor', 'Nurse', 'Pharmacist', 'RecordOfficer']
    job_title = jobs[option - 1]
    email = get_email()
    pass
def doctor():
    pass
def nurse():
    pass
def pharmacist():
    pass
def record_officer():
    pass
def exit():
    print('exiting...')
    sys.exit(0)

def login():
    print('LOG IN\n')
    username = input('Enter username: ')
    user = storage.get(Staff, 'username', username)
    if user:
        password = input('Enter your password: ')
        while not user.check_password(password):
            password = input('Enter your password: ')
    user = authenticate(email, password)
    if user:
        titles = ['Doctor', 'Nurse', 'Pharmacist', 'RecordOfficer']
        funcs = [doctor, nurse, pharmacist, record_officer]
        print('WELCOME f{user.staff_type} f{user.last_name}!')
        index = titles.index(user.job_title)
        funcs[index]()
    else:
        print('Too many tries')

def hmis():
    while True:
        print('WELCOME TO HMIS! HOW CAN WE HELP YOU?\n')
        print('1. LOG IN\t2. SIGN UP\t3. EXIT\n')
        choice = get_option('Choose option: ', [1, 2, 3])
        if choice == 1:
            login()
        elif choice == 2:
            signup()
        else:
            exit()
    
    
if __name__ == "__main__":
    hmis()
"""
# then import storage
"""

"""print('WELCOME TO HMIS DOCTOR SIGN UP PAGE, PLEASE ENTER THE FOLLOWING DETAILS\n')
# create a doctor object
doc = Doctor()
doc.first_name = input('First name: ')
doc.last_name = input('Last name: ')
doc.email = input('email: ')
year, month, day = input('Date of birth(YYYY-MM-DD): ').split('-')
doc.dob = date(int(year), int(month), int(day))
doc.set_password(input('password: '))
doc.save()
print('SIGNED UP SUCCESSFULLY!')
print('Welcome, Dr', doc.first_name, doc.last_name)

try:
    # empty the db
    subprocess.run(['./empty_db.sh'], check=True)
    print('\ndatabase emptied...\n')
except Exception as err:
    print(f'Emptying failed: {err}\n')
    exit(1)

# import storage to create all tables
from storage import storage

pprint = pprint.PrettyPrinter(indent=2).pprint

# create a doctor object
doc = Doctor()
doc.first_name = 'John'
doc.last_name = 'Doe'
doc.email = 'doc@hmis.com'
doc.dob = date(1758, 12, 12)
doc.set_password('doc_pwd')

doc.save()
print(doc, '\n')
print('NOTE BELOW THAT STAFF ID IS STILL AN INTEGER WITHIN THE DB\n')
print(f'new doctor __dict__: {doc.__dict__}', '\n')

pat = Patient()
pat.first_name = 'Pat'
pat.last_name = 'Doe'
pat.dob = date(1995, 8, 5)
pat.save()
print(pat, '\n')

print('First consultation')
consult_1 = Consultation()
consult_1.pid = pat.pid
consult_1.pc = "Fever x 5/7\nHeadache x 3/7\n"
consult_1.prov_diag = "Uncomplicated malaria"
consult_1.save()
print('CONSULTATION SAVED!')
print(consult_1, '\n')

print('Second consultation for the same patient')
consult_2 = Consultation()
consult_2.pid = pat.pid
consult_2.pc = "Neck Swelling x 5years\nHeadache x 1/52\n"
consult_2.prov_diag = "Goitre"
consult_2.save()
print('CONSULTATION SAVED!')
print(consult_2, '\n')
print('Above consultation was made for this patient:', consult_2.patient, '\n')

print(consult_1.patient == consult_2.patient, '\n')

print('All consultations for patient Pat Doe:', pat.consultations, '\n')

vitals_1 = VitalSign()
vitals_1.pid = pat.pid
vitals_1.consultation_id = consult_1.id
vitals_1.save()
print('VITAL SIGNS TAKEN!')
print(vitals_1, '\n')


print('The above vitals were recorded as part of:', vitals_1.consultation, '\n')

pres = Prescription()"""

