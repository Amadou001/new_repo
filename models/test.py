#!/usr/bin/python3
"""
from user import User
from agent import Agent
from property import Property
from transaction import Transaction
from whishlist import Whishlist
from property_image import Property_image
from visit_schedule import Visit_schedule
from payement import Payment
from review import Review
from base_model import Base
from message import Message
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://Amadou:Amadou2302&@localhost/training', pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

obj1 = User(firs_name="Amadou", last_name="Bah",  email="bamadou@gmail.com")
obj1.properties = [Property(title="Regalia"), Property(title="Noom")]
obj2 = Agent()
ob3 = Property()
obj4 = Transaction()
obj5 = Whishlist()
obj6 = Property_image()
obj7 = Visit_schedule()
obj8 = Message()
obj9 = Payment()
obj10 = Review()

#Base.metadata.create_all(bind=engine)

user = session.query(User).first()

session.delete(user)
session.commit()

session.add(obj1)
session.commit()
session.close()
"""

from engine.storage_db import DBStorage
storage = DBStorage()
#storage.reload()
print(storage.all())
