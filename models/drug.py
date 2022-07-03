#!/usr/bin/python3
"""Module for Drug class."""
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.sql import func
from models.base_model import Base
from models.base_model import BaseModel


class Drug(BaseModel, Base):
    """Class representing a Drug."""
    __tablename__ = "drugs"

    created_by = Column(Integer,
                        ForeignKey('pharmacists.staff_id', ondelete='SET NULL'))
    name = Column(String(60))
    dose = Column(String(60))
    route = Column(String(16))
    brand = Column(String(60))
    formulation = Column(String(60))
    expiry_date = Column(DateTime(timezone=True))
    stock_date = Column(DateTime(timezone=True), server_default=func.now())
    pharmacist = Column(String(60))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.created_by is not None:
            from storage import storage
            pharm = storage.get("Pharmacist", 'staff_id', self.created_by)
            self.pharmacist = f"{pharm.first_name} {pharm.last_name}"
