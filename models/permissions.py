#!/usr/bin/python3
"""Module for Permissions class"""


class Permission:
    """Class for permissions of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Permissions instance"""

        def __init__(self, create, edit, delete, view):
            self.create = create
            self.edit = edit
            self.delete = delete
            self.view = view
            
