#!/usr/bin/python3
"""Module for Permission class."""
from uuid import uuid4
from sqlalchemy import Column, String
from models.base_model import Base


class Permission(Base):
    """Class representing a Permissions."""
    __tablename__ = 'permissions'

    id = Column(String(60), primary_key=True, default=uuid4())
    name = Column(String(32), nullable=False, unique=True)
    __create = Column("create", String(128), nullable=False)
    __edit = Column("edit", String(128), nullable=False)
    __delete = Column("delete", String(128), nullable=False)
    __view = Column("view", String(128), nullable=False)

    @property
    def create(self):
        """create getter"""
        return self.__create

    @property
    def edit(self):
        """edit property getter"""
        return self.__edit

    @property
    def delete(self):
        """delete property getter"""
        return self.__delete

    @property
    def view(self):
        """view getter"""
        return self.__view
