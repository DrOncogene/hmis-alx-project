# HOSPITAL MANAGEMENT SOFTWARE (HMIS) PROJECT

MVP Specifications available at [Google Document](https://docs.google.com/document/d/1sZ9LaJosq4_ykBt08-fWQ58337GblLefScGzUmMjH0U/edit#heading=h.z6ne0og04bp5)  
Project landing page deployed [here](http://hmis-alx.netlify.app)  
Sample project to be deployed to (yet to be determined)

## Overview
Portfolio project done as part of the [ALX SE](www.alxafrica.com) foundation programme.  

The software, in the long term, is aimed at near total management of a hospital's activity ranging from patient consultation and nursing activities to pharmacy drug management.  

Technologies used in this project includes:  

Back-end:
  - Flask
  - Flasgger
  - SQLAlchemy
  - MySQL

Front-end:
  - HTML
  - CSS
  - ReactJS
  - etc.

## Components
1. Writing object models: BaseModel, BaseUser, Staff, Doctor, Nurse, Pharmacist, RecordOfficer, Consultation, Prescription, NurseNote, Vital, Drugs.
2. Database storage using ORM (sqlalchemy) and MySQL database backend
3. HMIS Console: command line utility written in python to manipulate objects
4. API using flask and flasgger
5. Front-end with HTML, CSS and ReactJS
6. Connect frontend to the backend
7. Deployment pipline with fabric, nginx and gunicorn on AWS EC2 ubuntu 22.04 instance

## The HMIS Console
Written with python's cmd module. Mainly for testing the models. Available commands are
- **help**: list all commands and their usage
- **quit**: exits the console
- **create \<class\>** or **\<class\>.create()**: intantiates a new object of the passed class
- **all [class], \<class\>.all()**: prints a list of all objects in storage or list of all object of type *class*
- **show \<class\> \<id\>, \<class\>.show(\<id\>)**: prints an object of a given class
- **destroy \<class\> \<id\>, \<class\>.destroy(\<id\>)**: deletes an obj of a given class
- **update \<class\> \<id\> \<dict\>, \<class\>.update(\<id\>, \<dict\>)**: updates the given object with values from dict
- **save**: commits all changes made to the db

## API
Written with flask and flasgger. Endpoints include

/api/v1/status  
GET: return a json object with message ‘OK’ or ‘FAIL’

/api/v1/stats  
GET: return a breakdown of all objects

/api/v1/patients  
GET: returns a list of all patients in the facility  
POST: creates a new patient object

/api/v1/patients/patient_id:  
GET: return the patient object with the given id  
PUT: modify the specified patient object  
DELETE: deletes the specified patient object

/api/v1/patients/patient_id/consultations  
GET: returns a list of all consultations attend by a given patient  
POST: create a new consultation for the given patient

/api/v1/patients/patient_id/consultations/consultation_id  
GET: returns the specified consultation for the given patient  
PUT: modify the specified consultation object, method to decay after 24 hours  
DELETE: deletes the specified consultation object, method to decay after creating object

/api/v1/patients/patient_id/consultations/consult_id/prescription  
GET: returns a list of drugs prescribed in a given consultation  
POST: create a new prescription for a consultation  
PUT: modify the specified prescription object, method to decay after 24 hours  
DELETE: deletes the specified prescription, method to decay after 24 hours

/api/v1/patients/patient_id/consult_id/prescription/drugs  
POST: add a new drug prescription to the prescription

/api/v1/patients/patient_id/consultations/consult_id/prescription/drugs/id  
PUT: modify the specified drug prescription object, to decay after 24 hours  
DELETE: deletes the specified drug prescription object, to decay after 24 hours

/api/v1/patients/patient_id/consultations/consult_id/vitals  
GET: returns a list of all vital signs recorded for the given patient  
POST: create a new vital sign object for the given patient

/api/v1/patients/patient_id/consultations/consult_id/vitals/vital_id  
GET: returns the vital sign object with the given id   
PUT: modify the vital sign object with the given id, decay after 24 hours  
DELETE: delete vital sign with the given id for the given patient, decay after 24 hours

/api/v1/patients/pid/nursenotes  
GET: return all nursenotes for a given patient  
POST: create a new nursenote for a patient

/api/v1/patients/pid/nursenotes/nursenote_id  
GET: return a specific nurse note  
PUT: update a nursenote

/api/v1/staffs  
GET: returns a breakdown of staffs in the facility

/api/v1/staffs/staff_id:  
GET: return specified objects and job title  
PUT: modify the specified staff object  
DELETE: deletes the specified staff object

/api/v1/staffs/doctors  
GET: returns a list of all doctors in the facility  
POST: creates a new doctor object

/api/v1/staffs/doctors/staff_id/consultations  
GET: returns a list of consultations for a given doctor in the facility

/api/v1/staffs/doctors/staff_id/prescriptions  
GET: returns a list of prescriptions for a given doctor in the facility

/api/v1/staffs/nurses  
GET: Returns a list of  all nurses in the facility  
POST: creates a new nurse object

/api/v1/staffs/nurses/staff_id/vitals  
GET: Returns the list of vitals obtained by the specified nurse

/api/v1/staffs/pharmacists  
GET: Returns a list of  all pharmacists in the facility  
POST: creates a new pharmacist object

/api/v1/staffs/pharmacists/staff_id/prescriptions  
GET: Returns the list of prescriptions dispensed by a pharmacist.

/api/v1/staffs/recordofficers  
GET: Returns a list of  all pharmacists in the facility  
POST: creates a new recordofficer object

/api/v1/drugs  
GET: return a list of all drugs in the pharmacy  
POST: create a new drug object

/api/v1/drugs/drug_id  
GET: return the specified drug object  
PUT: modify the given drug object

## Front-end static
In progress
