#!/usr/bin/python3
"""DB Storage module"""

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.agent import Agent
from models.user import User
from models.property import Property
from models.transaction import Transaction, Subcription
from models.whishlist import Whishlist
from models.review import Review
from models.property_image import Property_image
from models.message import Message, Room, RoomParticipants
base_dir = os.path.dirname(__file__)
parent_dir = os.path.join(base_dir, '..', '..')
sys_path = os.path.abspath(parent_dir)

sys.path.append(sys_path)


class DBStorage:
    """DBStorage
    Class to manage objects storage to DB
    """
    __engine = None
    __session = None

    def __init__(self):
        """Contructor method
        """
        env = os.getenv("env")
        url = "roofmarket_user:roofmarket_pwd@localhost/roofmarket_db"
        self.__engine = create_engine(
                    'mysql+mysqldb://' + url, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all to retrieve all records from DB

        Args:
            cls (string, optional): Object to return. Defaults to None.

        Returns:
            Dict: All records from a database
        """
        allclasses = {"User": User,
                      "Agent": Agent,
                      "Property": Property,
                      "Transaction": Transaction,
                      "Subcription": Subcription,
                      "Whishlist": Whishlist,
                      "Review": Review,
                      "Property_image": Property_image,
                      "Message": Message,
                      "Room": Room,
                      "RoomParticipants": RoomParticipants}
        obj_result = {}
        cls = cls if not isinstance(cls, str) else allclasses.get(cls)
        if cls is None:
            for cls in allclasses:
                objs = self.__session.query(cls).all()
                for o in objs:
                    obj_result["{}.{}".format(o.name, o.id)] = o
        else:
            objs = self.__session.query(cls).all()
            for o in objs:
                obj_result["{}.{}".format(o.__table__, o.id)] = o
        return obj_result

    def new(self, obj):
        """new : to add an an obj to a session

        Args:
            obj (instance): Obj created to be added
        """
        self.__session.add(obj)

    def save(self):
        """save: method to commit changes to the db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete an obj from the db

        Args:
            obj (string): name of the obj. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)

    def close(self):
        """close session
        """
        self.__session.remove() # use of remove instead of close in scooped_session

    def get_object(self, cls, sign=None, all=None, order_by=None,
                   limit=None,
                   count=False, **kwargs):
        """
        Get all objects or only one object based on filters.
        Optionally count the results.

        Args:
            cls: The model class to query.
            sign: The comparison operator for filtering.
            all: If not None, fetches all matching objects.
            order_by: A tuple (column, direction) for sorting
                (e.g., (cls.created_at, 'desc')).
            limit: An integer specifying the maximum number
                of results to return.
            count: If True, returns the count of results based on the filters.
            **kwargs: Key-value pairs for filtering.

        Returns:
            A single object if `all` is None, otherwise a list of objects.
            If `count` is True, returns the count of objects.
        """
        if sign is None:
            sign = '=='

        query = self.__session.query(cls)

        operators = {
            '==': lambda key, value: key == value,
            '!=': lambda key, value: key != value,
            '<': lambda key, value: key < value,
            '<=': lambda key, value: key <= value,
            '>': lambda key, value: key > value,
            '>=': lambda key, value: key >= value
        }

        if kwargs:
            for key, value in kwargs.items():
                if sign in operators:
                    query = query.filter(operators[sign](getattr(cls, key),
                                                         value))
                else:
                    raise ValueError(f"Invalid comparison operator: {sign}")
        if count:
            if (
                "room_id" in kwargs and
                "user_id" in kwargs and
                "read_status" in kwargs
            ):
                query = self.__session.query(cls).filter(
                    cls.room_id == kwargs.get("room_id"),
                    cls.user_id != kwargs.get("user_id"),
                    cls.read_status == False
                )

                return query.count()
        if order_by:
            column, direction = order_by
            if direction.lower() == 'desc':
                query = query.order_by(column.desc())
            elif direction.lower() == 'asc':
                query = query.order_by(column)
            else:
                raise ValueError("Invalid direction for order_by")

        if limit is not None:
            query = query.limit(limit)
        if all is not None:
            return query.all()
        return query.first()

    def property_objs(self, per_page, offset, property_type=None, country=None, 
                      city=None, max_price=None, min_price=None, listing_type=None):
        """ Returns the properties needed to be listed in one page"""

        if property_type:
            if country and city and max_price and min_price:
                return self.__session.query(Property).filter(Property.property_type == property_type, 
                                                             Property.country == country, Property.price <= max_price, 
                                                             Property.price >= min_price).limit(per_page).offset(offset)
            return self.__session.query(Property).filter(Property.property_type == property_type).limit(per_page).offset(offset)
        elif listing_type:
            return self.__session.query(Property).filter(Property.listing_type == listing_type).limit(per_page).offset(offset)
        return self.__session.query(Property).limit(per_page).offset(offset)

    def count(self, classe, property_type=None, country=None, 
              city=None, max_price=None, min_price=None, listing_type=None):
        """Counts the number of rows or objects in a given table sometimes with property_type given for properties"""
    
        if property_type:
            # Implemented for the search fonctionnality
            if country and city and max_price and min_price:
                return self.__session.query(classe).filter(classe.property_type == property_type, 
                                                           classe.country == country, classe.price <= max_price, 
                                                           classe.price >= min_price).count()
            return self.__session.query(classe).filter(classe.property_type == property_type).count()
        elif listing_type:
            # For filtering properties (sell, rent, ...)
            return self.__session.query(classe).filter(classe.listing_type == listing_type).count()
        return self.__session.query(classe).count()

    def get_image(self, property_id, image_type=None):
        """Returns a list of images or one image (if type) based on the property id"""
        if not image_type:
            return self.__session.query(Property_image).filter(Property_image.property_id == property_id).all()
        
        return self.__session.query(Property_image).filter(Property_image.property_id == property_id, 
                                                           Property_image.image_type == image_type).first()

    def get_countries(self):
        # Fetch distinct countries
        countries = self.__session.query(Property.country).distinct().all()
        countries_list = [country[0] for country in countries]
        return countries_list
    
    def get_cities(self, country):
        # Fetch distinct cities for the given country from the database
        return self.__session.query(Property.city).filter(Property.country == country).distinct().all()

    def get_property_by_id(self, property_id):
        """Returns the property of a specific id"""
        return self.__session.query(Property).filter(Property.id == property_id).first()
    
    def get_property_by_user_id(self, user_id, listing_type=None):
        """Returns all properties of the given user id"""
        if listing_type:
            return self.__session.query(Property).filter(Property.user_id == user_id, Property.listing_type == listing_type)
        return self.__session.query(Property).filter(Property.user_id == user_id)

    def delete_property_by_id(self, property_id):
        """Deletes a property matching the given id and its images"""
        self.__session.query(Property_image).filter(Property_image.property_id == property_id).delete()
        self.__session.query(Property).filter(Property.id == property_id).delete()
        self.__session.commit()
    
    def all_wishlist_for_user(self, user_id):
        """Returns a list of all user's wishlist"""
        ids= self.__session.query(Whishlist.property_id).filter(Whishlist.user_id == user_id).all()
        for id in ids:
            print(id)
        return ids
    
    def get_agents(self):
        """Returns all agent"""
        return self.__session.query(Agent).all()

