#!/usr/bin/python3
"""the auth package"""
from flask_login import LoginManager

from storage import storage
from models.staff import Staff


login_manager = LoginManager()
login_manager.login_view = 'auth_views.login'


@login_manager.user_loader
def load_user(user_id):
    """loads the user from db"""
    return storage.get(Staff, 'id', user_id)
