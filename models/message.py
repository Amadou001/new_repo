#!/usr/bin/python3
"""Message module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship


class Room(BaseModel, Base):
    """Mapping class for Room conversation"""
    __tablename__ = "room"
    roomparticipants = relationship("RoomParticipants", back_populates="room")
    message = relationship("Message", back_populates="room")


class RoomParticipants(BaseModel, Base):
    """Mapping class for Room participants"""
    __tablename__ = "roomparticipant"
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    property_id = Column(String(60), ForeignKey('property.id'))
    room_id = Column(String(60), ForeignKey('room.id'), nullable=False)
    room = relationship("Room", back_populates="roomparticipants")
    property = relationship("Property", back_populates="room_participants")
    user = relationship("User", back_populates="roomparticipants")
    room_position = Column(Boolean, default=False)


class Message(BaseModel, Base):
    """Mapping class for message table"""
    __tablename__ = "message"
    room_id = Column(String(60), ForeignKey('room.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    message = Column(Text, nullable=True)
    read_status = Column(Boolean, default=False)
    room = relationship("Room", back_populates="message")
