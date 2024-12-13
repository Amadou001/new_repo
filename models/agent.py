#!/usr/bin/python3
"""Agent module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Agent(BaseModel, Base):
    """Mapping class for agent table"""

    __tablename__ = "agent"

    agent_name= Column(String(60), nullable=False)
    image_url = Column(String(60), nullable=False)
