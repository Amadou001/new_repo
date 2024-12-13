#!/usr/bin/python3
"""property_image module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.property import Property
import os


class Property_image(BaseModel, Base):
    """Mapping class for property_image table"""
    __tablename__ = "property_image"
    image_type = Column(String(45), nullable=True)
    image_url = Column(String(400), nullable=True)
    property_id = Column(String(60), ForeignKey('property.id'), nullable=False)

        
    property2 = relationship("Property", back_populates="property_image")
