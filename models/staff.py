#!usr/bin/pyhton3
""" A class Staff that inherits from BaseUser """
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_user import BaseUser
from models.base_model import Base


class Staff(BaseUser, Base):
    """ Simple Staff class model """
    __tablename__ = 'staffs'

    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    staff_type = Column(String(16), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "staff",
        "polymorphic_on": staff_type
    }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def format_staff_id(self):
        titles = {
                "Admin": "ADM",
                "Doctor": "DOC",
                "Nurse": "NRS",
                "Pharmacist": "PHM",
                "RecordOfficer": "REC"
            }
        title = title = titles[self.__class__.__name__]
        return f'{title}{self.staff_id:04d}'
