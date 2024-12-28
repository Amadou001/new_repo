import unittest
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
from models.engine.storage_db import DBStorage

# FILE: test_storage_db.py


class TestDBStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a test database and session"""
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = scoped_session(cls.Session)
        cls.storage = DBStorage()
        cls.storage._DBStorage__session = cls.session

    @classmethod
    def tearDownClass(cls):
        """Tear down the test database"""
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """Set up for each test"""
        self.session = self.storage._DBStorage__session

    def tearDown(self):
        """Tear down for each test"""
        self.session.rollback()
        for tbl in reversed(Base.metadata.sorted_tables):
            self.session.execute(tbl.delete())
        self.session.commit()

    def test_all(self):
        """Test the all method"""
        user = User(name="Test User", email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.storage.save()
        result = self.storage.all("User")
        self.assertEqual(len(result), 1)

    def test_new(self):
        """Test the new method"""
        user = User(name="Test User", email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.assertIn(user, self.session)

    def test_save(self):
        """Test the save method"""
        user = User(name="Test User", email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.storage.save()
        self.assertEqual(self.session.query(User).count(), 1)

    def test_delete(self):
        """Test the delete method"""
        user = User(name="Test User", email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.storage.save()
        self.storage.delete(user)
        self.storage.save()
        self.assertEqual(self.session.query(User).count(), 0)

    def test_get_object(self):
        """Test the get_object method"""
        user = User(first_name="Test User", email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.storage.save()
        result = self.storage.get_object(User, first_name="Test User")
        self.assertEqual(result.first_name, "Test User")

    def test_property_objs(self):
        """Test the property_objs method"""
        property = Property(title="Test Property", user_id=1,
                            price=1000, description="Test Description")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.property_objs(10, 0)
        self.assertIn(property, result)

    def test_count(self):
        """Test the count method"""
        property = Property(title="Test Property", user_id=1,
                            price=1000, description="Test Description")
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
        property = Property(title="Test Property", country="Test Country",
                            user_id=1, price=1000,
                            description="Test Description")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_countries()
        self.assertIn("Test Country", result)

    def test_get_cities(self):
        """Test the get_cities method"""
        property = Property(title="Test Property",
                            country="Test Country", city="Test City",
                            user_id=1, price=1000,
                            description="Test Description")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_cities("Test Country")
        self.assertIn(("Test City",), result)

    def test_get_property_by_user_id(self):
        """Test the get_property_by_user_id method"""
        user = User(name="Test User", email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.storage.save()
        property = Property(user_id=user.id, title="Test Property")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_property_by_user_id(user.id)
        self.assertIn(property, result)

    def test_delete_property_by_id(self):
        """Test the delete_property_by_id method"""
        property = Property(id=1, title="Test Property",
                            user_id=1, price=1000,
                            description="Test Description")
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
        self.assertIn(('1',), result)

    def test_get_agents(self):
        """Test the get_agents method"""
        agent = Agent(agent_name="Test Agent", image_url="Test URL")
        self.storage.new(agent)
        self.storage.save()
        result = self.storage.get_agents()
        self.assertIn(agent, result)

    def test_get_object_with_limit(self):
        """Test get_object with limit"""
        user1 = User(name="User1", email="user1@example.com",
                     password_hash="hashed_password")
        user2 = User(name="User2", email="user2@example.com",
                     password_hash="hashed_password")
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        result = self.storage.get_object(User, all=True, limit=1)
        self.assertEqual(len(result), 1)

    def test_get_object_with_invalid_operator(self):
        """Test get_object with invalid operator"""
        with self.assertRaises(ValueError):
            self.storage.get_object(User, sign='invalid', name="User1")

    def test_property_objs_with_filters(self):
        """Test property_objs with filters"""
        property1 = Property(title="Property1", property_type="Type2",
                             country="Country1",
                             price=100, user_id=1)
        property2 = Property(title="Property2", property_type="Type1",
                             country="Country1",
                             price=300, user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.property_objs(10, 0, property_type="Type2",
                                            country="Country1", max_price=100,
                                            min_price=50)
        self.assertIn(property1, result)
        self.assertNotIn(property2, result)

    def test_count_with_filters(self):
        """Test count with filters"""
        property1 = Property(title="Property1", property_type="Type2",
                             country="Country1", price=100, user_id=1)
        property2 = Property(title="Property2", property_type="Type1",
                             country="Country1", price=200, user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.count(Property, property_type="Type2",
                                    country="Country1", max_price=150,
                                    min_price=50)
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
        property1 = Property(title="Property1", country="Country1",
                             city="City1", user_id=1)
        property2 = Property(title="Property2", country="Country2",
                             city="City2", user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_cities("Country1")
        self.assertIn(("City1",), result)
        self.assertNotIn("City2", result)

    def test_get_property_by_user_id_with_listing_type(self):
        """Test get_property_by_user_id with listing_type"""
        user = User(name="Test User", email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.storage.save()
        property1 = Property(user_id=user.id, listing_type="Type1",
                             title="Property1")
        property2 = Property(user_id=user.id, listing_type="Type2",
                             title="Property2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_property_by_user_id(user.id,
                                                      listing_type="Type1")
        self.assertIn(property1, result)
        self.assertNotIn(property2, result)

    def test_delete_property_by_id_with_images(self):
        """Test delete_property_by_id with images"""
        property = Property(id=1, title="Test Property", user_id=1,
                            price=1000, description="Test Description")
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
        self.assertIn(('1',), result)
        self.assertIn(('2',), result)

    def test_get_agents_with_multiple_agents(self):
        """Test get_agents with multiple agents"""
        agent1 = Agent(agent_name="Agent1", image_url="URL1")
        agent2 = Agent(agent_name="Agent2", image_url="URL2")
        self.storage.new(agent1)
        self.storage.new(agent2)
        self.storage.save()
        result = self.storage.get_agents()
        self.assertIn(agent1, result)
        self.assertIn(agent2, result)

    def test_get_object_with_multiple_filters(self):
        """Test get_object with multiple filters"""
        user1 = User(first_name="User1", email="user1@example.com",
                     password_hash="hashed_password")
        user2 = User(first_name="User2", email="user2@example.com",
                     password_hash="hashed_password")
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        result = self.storage.get_object(User, all=True,
                                         first_name="User1",
                                         email="user1@example.com")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].first_name, "User1")

    def test_property_objs_with_listing_type(self):
        """Test property_objs with listing_type"""
        property1 = Property(title="Property1",
                             listing_type="Type1", user_id=1)
        property2 = Property(title="Property2",
                             listing_type="Type2", user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.property_objs(10, 0,
                                            listing_type="Type1")
        self.assertIn(property1, result)
        self.assertNotIn(property2, result)

    def test_count_with_listing_type(self):
        """Test count with listing_type"""
        property1 = Property(title="Property1",
                             listing_type="Type1", user_id=1)
        property2 = Property(title="Property2",
                             listing_type="Type2", user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.count(Property, listing_type="Type1")
        self.assertEqual(result, 1)

    def test_get_image_with_invalid_property_id(self):
        """Test get_image with invalid property_id"""
        property = Property(id=1, title="Test Property",
                            user_id=1, price=1000,
                            description="Test Description")
        property_image = Property_image(property_id=1,
                                        image_type="Test Image")
        self.storage.new(property)
        self.storage.new(property_image)
        self.storage.save()
        result = self.storage.get_image(999)
        self.assertEqual(result, [])

    def test_get_countries_with_no_properties(self):
        """Test get_countries with no properties"""
        result = self.storage.get_countries()
        self.assertEqual(result, [])

    def test_get_cities_with_invalid_country(self):
        """Test get_cities with invalid country"""
        property = Property(title="Test Property",
                            country="Test Country",
                            city="Test City",
                            user_id=1, price=1000,
                            description="Test Description")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_cities("Invalid Country")
        self.assertEqual(result, [])

    def test_get_property_by_id_with_invalid_id(self):
        """Test get_property_by_id with invalid id"""
        property = Property(title="Test Property",
                            country="Test Country",
                            city="Test City",
                            user_id=1, price=1000,
                            description="Test Description")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_property_by_id(999)
        self.assertIsNone(result)

    def test_get_property_by_user_id_with_invalid_user_id(self):
        """Test get_property_by_user_id with invalid user_id"""
        property = Property(title="Test Property",
                            country="Test Country", city="Test City",
                            user_id=1, price=1000,
                            description="Test Description")
        self.storage.new(property)
        self.storage.save()
        result = self.storage.get_property_by_user_id(999)
        self.assertEqual(result.count(), 0)

    def test_delete_property_by_id_with_invalid_id(self):
        """Test delete_property_by_id with invalid id"""
        property = Property(title="Test Property",
                            country="Test Country", city="Test City",
                            user_id=1, price=1000,
                            description="Test Description")
        self.storage.new(property)
        self.storage.save()
        self.storage.delete_property_by_id(999)
        self.assertEqual(self.session.query(Property).count(), 1)

    def test_all_wishlist_for_user_with_invalid_user_id(self):
        """Test all_wishlist_for_user with invalid user_id"""
        wishlist1 = Whishlist(user_id=1, property_id=1)
        wishlist2 = Whishlist(user_id=1, property_id=2)
        self.storage.new(wishlist1)
        self.storage.new(wishlist2)
        self.storage.save()
        result = self.storage.all_wishlist_for_user(999)
        self.assertEqual(result, [])

    def test_get_agents_with_no_agents(self):
        """Test get_agents with no agents"""
        result = self.storage.get_agents()
        self.assertEqual(result, [])

    def test_get_object_with_invalid_class(self):
        """Test get_object with invalid class"""
        with self.assertRaises(NameError):
            self.storage.get_object("InvalidClass")

    def test_property_objs_with_invalid_filters(self):
        """Test property_objs with invalid filters"""
        property = Property(title="Test Property",
                            country="Test Country",
                            city="Test City",
                            user_id=1, price=1000,
                            property_type="Test type")
        result = self.storage.property_objs(10, 0,
                                            property_type="InvalidType")
        self.assertEqual(result.count(), 0)

    def test_get_image_with_invalid_image_type(self):
        """Test get_image with invalid image_type"""
        property = Property(id=1, title="Test Property",
                            user_id=1, price=1000,
                            description="Test Description")
        property_image = Property_image(property_id=1,
                                        image_type="Test Image")
        self.storage.new(property)
        self.storage.new(property_image)
        self.storage.save()
        result = self.storage.get_image(1, image_type="InvalidType")
        self.assertIsNone(result)

    def test_get_countries_with_multiple_properties(self):
        """Test get_countries with multiple properties"""
        property1 = Property(title="Property1",
                             country="Country1", user_id=1)
        property2 = Property(title="Property2",
                             country="Country2", user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_countries()
        self.assertIn("Country1", result)
        self.assertIn("Country2", result)

    def test_get_cities_with_multiple_cities(self):
        """Test get_cities with multiple cities"""
        property1 = Property(title="Property1",
                             country="Country1",
                             city="City1", user_id=1)
        property2 = Property(title="Property2",
                             country="Country1",
                             city="City2", user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_cities("Country1")
        self.assertIn(("City1",), result)
        self.assertIn(("City2",), result)

    def test_get_property_by_id_with_multiple_properties(self):
        """Test get_property_by_id with multiple properties"""
        property1 = Property(id=1, title="Property1",
                             user_id=1, price=1000,
                             description="Test Description")
        property2 = Property(id=2, title="Property2",
                             user_id=1, price=2000,
                             description="Test Description")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_property_by_id(1)
        self.assertEqual(result.title, "Property1")

    def test_get_property_by_user_id_with_multiple_properties(self):
        """Test get_property_by_user_id with multiple properties"""
        user = User(first_name="Test User",
                    email="test@example.com",
                    password_hash="hashed_password")
        self.storage.new(user)
        self.storage.save()
        property1 = Property(user_id=user.id, title="Property1")
        property2 = Property(user_id=user.id, title="Property2")
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        result = self.storage.get_property_by_user_id(user.id)
        self.assertIn(property1, result)
        self.assertIn(property2, result)

    def test_delete_property_by_id_with_multiple_properties(self):
        """Test delete_property_by_id with multiple properties"""
        property1 = Property(id=1, title="Property1", user_id=1)
        property2 = Property(id=2, title="Property2", user_id=1)
        self.storage.new(property1)
        self.storage.new(property2)
        self.storage.save()
        self.storage.delete_property_by_id(1)
        self.assertEqual(self.session.query(Property).count(), 1)

    def test_all_wishlist_for_user_with_multiple_users(self):
        """Test all_wishlist_for_user with multiple users"""
        user1 = User(first_name="User1",
                     email="user1@example.com",
                     password_hash="hashed_password")
        user2 = User(first_name="User2",
                     email="user2@example.com",
                     password_hash="hashed_password")
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        wishlist1 = Whishlist(user_id=user1.id, property_id=1)
        wishlist2 = Whishlist(user_id=user2.id, property_id=2)
        self.storage.new(wishlist1)
        self.storage.new(wishlist2)
        self.storage.save()
        result = self.storage.all_wishlist_for_user(user1.id)
        self.assertIn(('1',), result)
        self.assertNotIn(('2',), result)

    def test_get_agents_with_multiple_agents(self):
        """Test get_agents with multiple agents and properties"""
        agent1 = Agent(agent_name="Agent1", image_url="URL1")
        agent2 = Agent(agent_name="Agent2", image_url="URL2")
        self.storage.new(agent1)
        self.storage.new(agent2)
        self.storage.save()
        result = self.storage.get_agents()
        self.assertIn(agent1, result)
        self.assertIn(agent2, result)


if __name__ == '__main__':
    unittest.main()
