#!/usr/bin/python3
"""Module for Drug class."""
from sqlalchemy import Column, String, DateTime
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
    expiry_date = Column(DateTime(timezone=True))
    stock_date = Column(DateTime(timezone=True))
