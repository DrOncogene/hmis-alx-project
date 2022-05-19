#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
all_objects = storage.all()
staff_ids = []
patient_ids = []
for key, value in all_objects.items():
    if key.split(".")[0] == "Staff":
        staff_ids.append(value.id)
    if key.split(".")[0] == "Patient":
        patient_ids.append(value.id)
