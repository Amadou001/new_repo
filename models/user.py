#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from models.property import Property
from models.transaction import Transaction
from models.whishlist import Whishlist
from models.message import Message
from models.review import Review
from werkzeug.security import generate_password_hash, check_password_hash
import os


class User(BaseModel, Base, UserMixin):
    """Mapping class for user table"""
    __tablename__ = "user"
    first_name = Column(String(224), nullable=True)
    last_name = Column(String(224), nullable=True)
    email = Column(String(224), nullable=True, unique=True)
    phone_number = Column(String(45), nullable=True)
    password_hash = Column(String(1024), nullable=True)
    user_type = Column(String(10), nullable=True)
    profile_image = Column(String(65), nullable=True)
    is_online = Column(Boolean, nullable=False, default=False)

    properties = relationship("Property", back_populates="user",
                              cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="user",
                                cascade="all, delete-orphan")
    whishlists = relationship("Whishlist", back_populates="user",
                              cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user",
                           cascade="all, delete-orphan")
    roomparticipants = relationship("RoomParticipants", back_populates="user")


    @property
    def password(self):
        raise AttributeError('Password is not a readable Attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)

    def __str__(self):
        return '<User %r>' % User.id
