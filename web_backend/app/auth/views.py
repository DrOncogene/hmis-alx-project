#!/usr/bin/python3
"""Defines the authentication views"""
from flask import Blueprint, jsonify, request, abort
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf.csrf import generate_csrf

from storage import storage

auth_views = Blueprint("auth_views", __name__, url_prefix="/auth")


@auth_views.route("/login", methods=["POST"])
def login():
    """the login method"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    if ('username' not in data) and ('email' not in data):
        abort(400, description="missing username or email")

    username = data.get('username', None)
    email = data.get('email', None)
    if username:
        user = storage.get("Staff", 'username', username)
    elif email:
        user = storage.get("Staff", 'email', email)

    if not user:
        return jsonify({"login": "failed"}), 404

    password = data.get('password', None)
    if not password:
        abort(400, description="missing password")

    if not user.check_password(password):
        return jsonify({"login": False}), 404

    login_user(user, remember=True)
    return jsonify({"login": True})


@auth_views.route('/getcsrf', methods=['GET'])
def create_csrf():
    """generates a new csrf token"""
    token = generate_csrf()
    response = jsonify({'csrf': 'cookie set'})
    response.headers.set('X-CSRFToken', token)

    return response


@auth_views.route('/isauthenticated')
def is_authenticated():
    """checks whether a user is already authenticated"""
    print(request.headers)
    if current_user.is_authenticated:
        return jsonify({'login': True})

    return jsonify({'login': False}), 401


@auth_views.route('/logout')
@login_required
def logout():
    """logout the current user"""
    if not current_user.is_authenticated:
        abort(404, description="Not logged in")

    logout_user()
    return jsonify({"logout": True})
