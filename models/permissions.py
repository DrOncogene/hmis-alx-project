#!/usr/bin/python3
"""Module for Permission class."""


class Permission:
    """Class representing a Permissions."""
    def __init__(self, create, edit, delete, view):
        self.__create = create
        self.__edit = edit
        self.__delete = delete
        self.__view = view

    @property
    def create(self):
        return self.__create

    @property
    def edit(self):
        return self.__edit

    @property
    def delete(self):
        return self.__delete

    @property
    def view(self):
        return self.__view
