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
    __create = Column(String(128), nullable=False)
    __edit = Column(String(128), nullable=False)
    __delete = Column(String(128), nullable=False)
    __view = Column(String(128), nullable=False)

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
