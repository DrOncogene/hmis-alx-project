#!/usr/bin/python3
"""Module for Permission class."""
from uuid import uuid4
from sqlalchemy import Column, String, Enum
from models.base_model import Base


class Permission(Base):
    """Class representing a Permissions."""
    __tablename__ = 'permissions'

    id = Column(String(60), primary_key=True, default=uuid4())
    name = Column(String(32), nullable=False, unique=True)
    create = Column(String(128), nullable=False)
    edit = Column(String(128), nullable=False)
    delete = Column(String(128), nullable=False)
    view = Column(String(128), nullable=False)

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
