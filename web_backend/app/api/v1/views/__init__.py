#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint

api_views = Blueprint("api_views", __name__, url_prefix="/api/v1")

from .index import *  # noqa E402
from .patient import *  # noqa E402
from .staff import *  # noqa E402
from .doctor import *  # noqa E402
from .nurse import *  # noqa E402
from .pharmacist import *  # noqa E402
from .drug import *  # noqa E402
from .consult import *  # noqa E402
from .prescription import *  # noqa E402
from .vitals import *  # noqa E402
from .nursenote import *  # noqa E402
