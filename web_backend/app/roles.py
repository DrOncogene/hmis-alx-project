#!/usr/bin/python3
"""decorators for role based access control"""
from functools import wraps

from flask_login import current_user
from flask import abort, request


class RBAC:
    """define decorators for rbac"""
    @staticmethod
    def allow(roles, methods=None):
        """allows certain roles"""
        def allow_decorator(view_func):
            @wraps(view_func)
            def wrapper(*args, **kwargs):
                method_valid = request.method in methods if methods else True
                role_valid = current_user and current_user.role in roles
                if not (method_valid and role_valid):
                    abort(401, description="Not priviledged")
                return view_func(*args, **kwargs)
            return wrapper
        return allow_decorator
