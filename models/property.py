#!/usr/bin/python3
"""property module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.transaction import Transaction
from models.whishlist import Whishlist
from models.message import Message
from models.review import Review
import os

class Property(BaseModel, Base):
    """Mapping class for property table"""

    __tablename__ = "property"
    title = Column(String(50), nullable=True)
    description = Column(String(2050), nullable=True)
    property_type = Column(String(10), nullable=True)
    price = Column(Float, nullable=True)
    listing_type = Column(String(5), nullable=True)
    address = Column(String(224), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    country = Column(String(50), nullable=True)
    zip_code = Column(String(15), nullable=True)
    bedrooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)
    area = Column(Float, nullable=True)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="properties")
    transaction = relationship("Transaction", back_populates="property1", cascade="all, delete-orphan")
    property_image = relationship("Property_image", back_populates="property2", cascade="all, delete-orphan")
    whishlists = relationship("Whishlist", back_populates="properties")
    room_participants = relationship("RoomParticipants", back_populates="property")
    reviews = relationship("Review", back_populates="property")
