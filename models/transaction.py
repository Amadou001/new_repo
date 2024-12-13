#!/usr/bin/python3
"""transaction module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Float, String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
import os

class Transaction(BaseModel, Base):
    """Mapping class for transaction table"""

    __tablename__ = "transaction"
    payment_status = Column(String(10), nullable=True)
    supplier_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    property_id = Column(String(60), ForeignKey('property.id'), nullable=False)
    duration = Column(Integer)

    user = relationship("User", back_populates="transactions")

    property1 = relationship("Property", back_populates="transaction")



class Subcription(BaseModel, Base):
    """Subcription status"""
    __tablename__ = "subcription"
    status = Column(String(9))
