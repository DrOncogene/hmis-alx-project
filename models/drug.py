#!/usr/bin/python3
"""Module for Drug class."""
from datetime import datetime
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from models.base_model import Base
from models.base_model import BaseModel


class Drug(BaseModel, Base):
    """Class representing a Drug."""
    __tablename__ = "drugs"

    name = Column(String(60))
    dose = Column(String(60))
    route = Column(String(16))
    brand = Column(String(60))
    formulation = Column(String(60))
    expiry_date = Column(TIMESTAMP)
    stock_date = Column(TIMESTAMP, default=datetime.now())
