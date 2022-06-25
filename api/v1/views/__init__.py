#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.patient import *
from api.v1.views.staff import *
from api.v1.views.doctor import *
from api.v1.views.nurses import *
from api.v1.views.pharmacist import *
from api.v1.views.drug import *
from api.v1.views.consult import *
from api.v1.views.prescription import *
from api.v1.views.vitals import *
from api.v1.views.nursenote import *
