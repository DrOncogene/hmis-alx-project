#!/usr/bin/python3
"""This module instantiates a storage object"""
from storage.dbs import DBStorage

storage = DBStorage()
storage.reload()
