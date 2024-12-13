#!/usr/bin/python3
"""Review module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os

class Review(BaseModel, Base):
    """Mapping class for review table"""

    __tablename__ = "review"
    rating = Column(Integer, nullable=True)
    comment = Column(String(1023), nullable=True)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    property_id = Column(String(60), ForeignKey('property.id'), nullable=False)


    user = relationship("User", back_populates="reviews")
    property = relationship("Property", back_populates="reviews")
