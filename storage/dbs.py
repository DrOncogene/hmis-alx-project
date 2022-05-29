#!/usr/bin/python3
""" module that defines the db storage engine"""
from os import getenv as osgetenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.patient import Patient
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from models.notes.consult import Consultation
from models.notes.prescription import Prescription
from models.notes.vitals import VitalSign
from models.notes.nursenote import NurseNote
from models.drug import Drug


class DBStorage:
    """ the db storage class"""
    __engine = None
    __session = None
    _classes = [Patient, Doctor, Nurse, Pharmacist, RecordOfficer, Admin,
                Consultation, Prescription, VitalSign, NurseNote, Drug]

    def __init__(self):
        user = osgetenv('DB_USER')
        passwd = osgetenv('DB_PWD')
        host = osgetenv('DB_HOST')
        db = osgetenv('DB')
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(user, passwd, host, db),
            pool_pre_ping=True
        )
        if osgetenv('ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ queries the db for all objects"""
        session = self.__session
        obj_list = []
        obj_dict = {}
        if cls is None:
            for obj_cls in self._classes:
                obj_list.extend(session.query(obj_cls).all())
            for obj in obj_list:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict.update({key: obj})
            return obj_dict
        for obj_cls in self._classes:
            if obj_cls == cls:
                obj_list.extend(session.query(obj_cls).all())
                break
        for obj in obj_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict.update({key: obj})

        return obj_dict

    def new(self, obj):
        """ adds a new obj to the db session"""
        self.__session.add(obj)

    def save(self):
        """ commits all changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from the current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ creates all db tables"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__sessionmaker = scoped_session(factory)
        self.__session = self.__sessionmaker()

    def close(self):
        """ remove the current session and create a new one"""
        self.__session.close()
        self.__session = self.__sessionmaker()
