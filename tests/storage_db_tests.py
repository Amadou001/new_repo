import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.agent import Agent
from models.user import User
from models.property import Property
from models.transaction import Transaction, Subcription
from models.whishlist import Whishlist
from models.review import Review
from models.property_image import Property_image
from models.message import Message, Room, RoomParticipants
from models.engine.storage_db import DBStorage

# FILE: test_storage_db.py


class TestDBStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a test database and session"""
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.storage = DBStorage()
        cls.storage._DBStorage__session = cls.session

    @classmethod
    def tearDownClass(cls):
        """Tear down the test database"""
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """Set up a new session for each test"""
        self.session = self.Session()
        self.storage._DBStorage__session = self.session

    def tearDown(self):
        """Rollback any changes made during the test"""
        self.session.rollback()
        self.session.close()

    def test_all(self):
        """Test the all method"""
        user = User(name="Test User")
        self.storage.new(user)
        self.storage.save()
        result = self.storage.all("User")
        self.assertIn("User.1", result)

    def test_new(self):
        """Test the new method"""
        user = User(name="Test User")
        self.storage.new(user)
        self.assertIn(user, self.session)

    def test_save(self):
        """Test the save method"""
        user = User(name="Test User")
        self.storage.new(user)
        self.storage.save()
        self.assertEqual(self.session.query(User).count(), 1)

    def test_delete(self):
        """Test the delete method"""
        user = User(name="Test User")
        self.storage.new(user)
        self.storage.save()
        self.storage.delete(user)
        self.assertEqual(self.session.query(User).count(), 0)

    def test_reload(self):
        """Test the reload method"""
        self.storage.reload()
        self.assertIsNotNone(self.storage._DBStorage__session)

    def test_close(self):
        """Test the close method"""
        self.storage.reload()
        self.storage.close()
        self.assertRaises(Exception, self.storage._DBStorage__session.query, User)

    def test_get_object(self):
        """Test the get_object method"""
        user = User(name="Test User")
        self.storage.new(user)
        self.storage.save()
        result = self.storage.get_object(User, name="Test User")
        self.assertEqual(result.name, "Test User")

    def test_property_objs(self):
        """Test the property_objs method"""
        property = Property(name="Test Property")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.property_objs(10, 0)
        self.assertIn(property, result)

    def test_count(self):
        """Test the count method"""
        property = Property(name="Test Property")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.count(Property)
        self.assertEqual(result, 1)

    def test_get_image(self):
        """Test the get_image method"""
        property_image = Property_image(property_id=1, image_type="Test Image")
        self.storage.new(property_image)
        self.storage.save()
        result = self.storage.get_image(1)
        self.assertIn(property_image, result)

    def test_get_countries(self):
        """Test the get_countries method"""
        property = Property(country="Test Country")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_countries()
        self.assertIn("Test Country", result)

    def test_get_cities(self):
        """Test the get_cities method"""
        property = Property(country="Test Country", city="Test City")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_cities("Test Country")
        self.assertIn("Test City", result)

    def test_get_property_by_id(self):
        """Test the get_property_by_id method"""
        property = Property(id=1, name="Test Property")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_property_by_id(1)
        self.assertEqual(result.name, "Test Property")

    def test_get_property_by_user_id(self):
        """Test the get_property_by_user_id method"""
        property = Property(user_id=1, name="Test Property")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_property_by_user_id(1)
        self.assertIn(property, result)

    def test_delete_property_by_id(self):
        """Test the delete_property_by_id method"""
        property = Property(id=1, name="Test Property")
        self.storage.new(property)
        self.storage.save()
        self.storage.delete_property_by_id(1)
        self.assertEqual(self.session.query(Property).count(), 0)

    def test_all_wishlist_for_user(self):
        """Test the all_wishlist_for_user method"""
        wishlist = Whishlist(user_id=1, property_id=1)
        self.storage.new(wishlist)
        self.storage.save()
        result = self.storage.all_wishlist_for_user(1)
        self.assertIn((1,), result)

    def test_get_agents(self):
        """Test the get_agents method"""
        agent = Agent(name="Test Agent")
        self.storage.new(agent)
        self.storage.save()
        result = self.storage.get_agents()
        self.assertIn(agent, result)

    # Additional tests to reach at least 70 tests
    def test_get_object_with_limit(self):
        """Test get_object with limit"""
        user1 = User(name="User1")
        user2 = User(name="User2")
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        result = self.storage.get_object(User, all=True, limit=1)
        self.assertEqual(len(result), 1)

    def test_get_object_with_order_by(self):
        """Test get_object with order_by"""
        user1 = User(name="User1")
        user2 = User(name="User2")
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        result = self.storage.get_object(User, all=True, order_by=(User.name, 'asc'))
        self.assertEqual(result[0].name, "User1")

    def test_get_object_with_invalid_operator(self):
        """Test get_object with invalid operator"""
        with self.assertRaises(ValueError):
            self.storage.get_object(User, sign='invalid', name="User1")

    def test_property_objs_with_filters(self):
        """Test property_objs with filters"""
        property1 = Property(name="Property1", property_type="Type1", country="Country1", price=100)
        property2 = Property(name="Property2", property_type="Type1", country="Country1", price=200)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.property_objs(10, 0, property_type="Type1", country="Country1", max_price=150, min_price=50)
        self.assertIn(property1, result)
        self.assertNotIn(property2, result)

    def test_count_with_filters(self):
        """Test count with filters"""
        property1 = Property(name="Property1", property_type="Type1", country="Country1", price=100)
        property2 = Property(name="Property2", property_type="Type1", country="Country1", price=200)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.count(Property, property_type="Type1", country="Country1", max_price=150, min_price=50)
        self.assertEqual(result, 1)

    def test_get_image_with_type(self):
        """Test get_image with type"""
        property_image1 = Property_image(property_id=1, image_type="Type1")
        property_image2 = Property_image(property_id=1, image_type="Type2")
        self.storage.new(property_image1)
        self.storage.new(property_image2)
        self.storage.save()
        result = self.storage.get_image(1, image_type="Type1")
        self.assertEqual(result, property_image1)

    def test_get_cities_with_no_country(self):
        """Test get_cities with no country"""
        property1 = Property(country="Country1", city="City1")
        property2 = Property(country="Country2", city="City2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_cities("Country1")
        self.assertIn("City1", result)
        self.assertNotIn("City2", result)

    def test_get_property_by_user_id_with_listing_type(self):
        """Test get_property_by_user_id with listing_type"""
        property1 = Property(user_id=1, listing_type="Type1")
        property2 = Property(user_id=1, listing_type="Type2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_property_by_user_id(1, listing_type="Type1")
        self.assertIn(property1, result)
        self.assertNotIn(property2, result)

    def test_delete_property_by_id_with_images(self):
        """Test delete_property_by_id with images"""
        property = Property(id=1, name="Test Property")
        property_image = Property_image(property_id=1, image_type="Test Image")
        self.storage.new(property)
        self.storage.new(property_image)
        self.storage.save()
        self.storage.delete_property_by_id(1)
        self.assertEqual(self.session.query(Property).count(), 0)
        self.assertEqual(self.session.query(Property_image).count(), 0)

    def test_all_wishlist_for_user_with_multiple_entries(self):
        """Test all_wishlist_for_user with multiple entries"""
        wishlist1 = Whishlist(user_id=1, property_id=1)
        wishlist2 = Whishlist(user_id=1, property_id=2)
        self.storage.new(wishlist1)
        self.storage.new(wishlist2)
        self.storage.save()
        result = self.storage.all_wishlist_for_user(1)
        self.assertIn((1,), result)
        self.assertIn((2,), result)

    def test_get_agents_with_multiple_agents(self):
        """Test get_agents with multiple agents"""
        agent1 = Agent(name="Agent1")
        agent2 = Agent(name="Agent2")
        self.storage.new(agent1)
        self.storage.new(agent2)
        self.storage.save()
        result = self.storage.get_agents()
        self.assertIn(agent1, result)
        self.assertIn(agent2, result)

    # Add more tests to reach at least 70 tests
    def test_get_object_with_multiple_filters(self):
        """Test get_object with multiple filters"""
        user1 = User(name="User1", email="user1@example.com")
        user2 = User(name="User2", email="user2@example.com")
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        result = self.storage.get_object(User, all=True, name="User1", email="user1@example.com")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "User1")

    def test_property_objs_with_listing_type(self):
        """Test property_objs with listing_type"""
        property1 = Property(name="Property1", listing_type="Type1")
        property2 = Property(name="Property2", listing_type="Type2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.property_objs(10, 0, listing_type="Type1")
        self.assertIn(property1, result)
        self.assertNotIn(property2, result)

    def test_count_with_listing_type(self):
        """Test count with listing_type"""
        property1 = Property(name="Property1", listing_type="Type1")
        property2 = Property(name="Property2", listing_type="Type2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.count(Property, listing_type="Type1")
        self.assertEqual(result, 1)

    def test_get_image_with_invalid_property_id(self):
        """Test get_image with invalid property_id"""
        result = self.storage.get_image(999)
        self.assertEqual(result, [])

    def test_get_countries_with_no_properties(self):
        """Test get_countries with no properties"""
        result = self.storage.get_countries()
        self.assertEqual(result, [])

    def test_get_cities_with_invalid_country(self):
        """Test get_cities with invalid country"""
        result = self.storage.get_cities("Invalid Country")
        self.assertEqual(result, [])

    def test_get_property_by_id_with_invalid_id(self):
        """Test get_property_by_id with invalid id"""
        result = self.storage.get_property_by_id(999)
        self.assertIsNone(result)

    def test_get_property_by_user_id_with_invalid_user_id(self):
        """Test get_property_by_user_id with invalid user_id"""
        result = self.storage.get_property_by_user_id(999)
        self.assertEqual(result.count(), 0)

    def test_delete_property_by_id_with_invalid_id(self):
        """Test delete_property_by_id with invalid id"""
        self.storage.delete_property_by_id(999)
        self.assertEqual(self.session.query(Property).count(), 0)

    def test_all_wishlist_for_user_with_invalid_user_id(self):
        """Test all_wishlist_for_user with invalid user_id"""
        result = self.storage.all_wishlist_for_user(999)
        self.assertEqual(result, [])

    def test_get_agents_with_no_agents(self):
        """Test get_agents with no agents"""
        result = self.storage.get_agents()
        self.assertEqual(result, [])

    def test_get_object_with_invalid_class(self):
        """Test get_object with invalid class"""
        with self.assertRaises(AttributeError):
            self.storage.get_object("InvalidClass")

    def test_property_objs_with_invalid_filters(self):
        """Test property_objs with invalid filters"""
        result = self.storage.property_objs(10, 0, property_type="InvalidType")
        self.assertEqual(result.count(), 0)

    def test_count_with_invalid_filters(self):
        """Test count with invalid filters"""
        result = self.storage.count(Property, property_type="InvalidType")
        self.assertEqual(result, 0)

    def test_get_image_with_invalid_image_type(self):
        """Test get_image with invalid image_type"""
        result = self.storage.get_image(1, image_type="InvalidType")
        self.assertIsNone(result)

    def test_get_countries_with_multiple_properties(self):
        """Test get_countries with multiple properties"""
        property1 = Property(country="Country1")
        property2 = Property(country="Country2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_countries()
        self.assertIn("Country1", result)
        self.assertIn("Country2", result)

    def test_get_cities_with_multiple_cities(self):
        """Test get_cities with multiple cities"""
        property1 = Property(country="Country1", city="City1")
        property2 = Property(country="Country1", city="City2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_cities("Country1")
        self.assertIn("City1", result)
        self.assertIn("City2", result)

    def test_get_property_by_id_with_multiple_properties(self):
        """Test get_property_by_id with multiple properties"""
        property1 = Property(id=1, name="Property1")
        property2 = Property(id=2, name="Property2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_property_by_id(1)
        self.assertEqual(result.name, "Property1")

    def test_get_property_by_user_id_with_multiple_properties(self):
        """Test get_property_by_user_id with multiple properties"""
        property1 = Property(user_id=1, name="Property1")
        property2 = Property(user_id=1, name="Property2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_property_by_user_id(1)
        self.assertIn(property1, result)
        self.assertIn(property2, result)

    def test_delete_property_by_id_with_multiple_properties(self):
        """Test delete_property_by_id with multiple properties"""
        property1 = Property(id=1, name="Property1")
        property2 = Property(id=2, name="Property2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        self.storage.delete_property_by_id(1)
        self.assertEqual(self.session.query(Property).count(), 1)

    def test_all_wishlist_for_user_with_multiple_users(self):
        """Test all_wishlist_for_user with multiple users"""
        wishlist1 = Whishlist(user_id=1, property_id=1)
        wishlist2 = Whishlist(user_id=2, property_id=2)
        self.storage.new(wishlist1)
        self.storage.new(wishlist2)
        self.storage.save()
        result = self.storage.all_wishlist_for_user(1)
        self.assertIn((1,), result)
        self.assertNotIn((2,), result)

    def test_get_agents_with_multiple_agents_and_properties(self):
        """Test get_agents with multiple agents and properties"""
        agent1 = Agent(name="Agent1")
        agent2 = Agent(name="Agent2")
        property1 = Property(agent_id=1, name="Property1")
        property2 = Property(agent_id=2, name="Property2")
        self.storage.new(agent1)
        self.storage.new(agent2)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_agents()
        self.assertIn(agent1, result)
        self.assertIn(agent2, result)

if __name__ == '__main__':
    unittest.main()
