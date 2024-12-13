#!/usr/bin/python3
"""Whishlist module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Whishlist(BaseModel, Base):
    """Mapping class for whishlist table"""
    __tablename__ = "whishlist"
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    property_id = Column(String(60), ForeignKey('property.id'), nullable=False)

    user = relationship("User", back_populates="whishlists")

    properties = relationship("Property", back_populates="whishlists")


    