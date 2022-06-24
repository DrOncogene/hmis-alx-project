#!/usr/bin/python3
""" module that defines the db storage engine"""
from os import getenv as osgetenv
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import OperationalError, IntegrityError
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
    __sessionmaker = None
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
        if cls is None:
            for obj_cls in self._classes:
                obj_list.extend(session.query(obj_cls).all())
        else:
            obj_list = session.query(cls).all()

        return obj_list

    def get(self, cls: type, attr: str, val: str):
        """returns a single obj of cls with id"""
        if attr == 'staff_id':
            obj = self.__session.query(cls).filter_by(staff_id=val).first()
        elif attr == 'pid':
            obj = self.__session.query(cls).filter_by(pid=val).first()
        elif attr == 'username':
            obj = self.__session.query(cls).filter_by(username=val).first()
        elif attr == 'email':
            obj = self.__session.query(cls).filter_by(email=val).first()
        else:
            obj = self.__session.query(cls).filter_by(id=val).first()
        return obj

    def count(self, cls=None):
        """ count the number of objs in storage of cls, if given"""
        return len(self.all(cls))

    def new(self, obj):
        """ adds a new obj to the db session"""
        self.__session.add(obj)

    def save(self):
        """ commits all changes to db"""
        try:
            self.__session.commit()
        except Exception as err:
            self.__session.rollback()
            print(err)

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
