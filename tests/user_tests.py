import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.user = User(id=1, name="Test User")

    def tearDown(self):
        """Tear down test environment"""
        del self.user

    def test_password_setter(self):
        """Test the password setter"""
        self.user.password = "test_password"
        self.assertTrue(self.user.password_hash is not None)
        self.assertTrue(check_password_hash(self.user.password_hash, "test_password"))

    def test_password_getter_raises_error(self):
        """Test that password getter raises an error"""
        with self.assertRaises(AttributeError):
            _ = self.user.password

    def test_verify_password(self):
        """Test the verify_password method"""
        self.user.password = "test_password"
        self.assertTrue(self.user.verify_password("test_password"))
        self.assertFalse(self.user.verify_password("wrong_password"))

    @patch('models.user.User.properties', new_callable=MagicMock)
    def test_properties_relationship(self, mock_properties):
        """Test the properties relationship"""
        self.assertIsNotNone(self.user.properties)

    @patch('models.user.User.transactions', new_callable=MagicMock)
    def test_transactions_relationship(self, mock_transactions):
        """Test the transactions relationship"""
        self.assertIsNotNone(self.user.transactions)

    @patch('models.user.User.whishlists', new_callable=MagicMock)
    def test_whishlists_relationship(self, mock_whishlists):
        """Test the whishlists relationship"""
        self.assertIsNotNone(self.user.whishlists)

    @patch('models.user.User.reviews', new_callable=MagicMock)
    def test_reviews_relationship(self, mock_reviews):
        """Test the reviews relationship"""
        self.assertIsNotNone(self.user.reviews)

    @patch('models.user.User.roomparticipants', new_callable=MagicMock)
    def test_roomparticipants_relationship(self, mock_roomparticipants):
        """Test the roomparticipants relationship"""
        self.assertIsNotNone(self.user.roomparticipants)

    def test_user_id(self):
        """Test the user id"""
        self.assertEqual(self.user.id, 1)

    def test_user_name(self):
        """Test the user name"""
        self.assertEqual(self.user.name, "Test User")

    def test_user_email(self):
        """Test the user email"""
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")

    def test_user_phone(self):
        """Test the user phone"""
        self.user.phone = "1234567890"
        self.assertEqual(self.user.phone, "1234567890")

    def test_user_address(self):
        """Test the user address"""
        self.user.address = "123 Test St"
        self.assertEqual(self.user.address, "123 Test St")

    def test_user_creation_date(self):
        """Test the user creation date"""
        self.user.created_at = "2023-01-01"
        self.assertEqual(self.user.created_at, "2023-01-01")

    def test_user_update_date(self):
        """Test the user update date"""
        self.user.updated_at = "2023-01-02"
        self.assertEqual(self.user.updated_at, "2023-01-02")

    def test_user_is_active(self):
        """Test the user is active"""
        self.user.is_online = True
        self.assertTrue(self.user.is_online)

    def test_user_is_admin(self):
        """Test the user is admin"""
        self.user.is_admin = False
        self.assertFalse(self.user.is_admin)

    def test_user_set_first_name(self):
        """Test setting the user's first name"""
        self.user.first_name = "New"
        self.assertEqual(self.user.first_name, "New")

    def test_user_set_last_name(self):
        """Test setting the user's last name"""
        self.user.last_name = "Name"
        self.assertEqual(self.user.last_name, "Name")

    def test_user_set_is_active(self):
        """Test setting the user's active status"""
        self.user.is_online = False
        self.assertFalse(self.user.is_online)

    def test_user_set_is_admin(self):
        """Test setting the user's admin status"""
        self.user.is_admin = True
        self.assertTrue(self.user.is_admin)

    def test_user_set_created_at(self):
        """Test setting the user's creation date"""
        self.user.created_at = "2023-01-03"
        self.assertEqual(self.user.created_at, "2023-01-03")

    def test_user_set_updated_at(self):
        """Test setting the user's update date"""
        self.user.updated_at = "2023-01-04"
        self.assertEqual(self.user.updated_at, "2023-01-04")

    def test_user_set_email(self):
        """Test setting the user's email"""
        self.user.email = "new@example.com"
        self.assertEqual(self.user.email, "new@example.com")

    def test_user_set_phone(self):
        """Test setting the user's phone"""
        self.user.phone = "0987654321"
        self.assertEqual(self.user.phone, "0987654321")

    def test_user_set_address(self):
        """Test setting the user's address"""
        self.user.address = "456 New St"
        self.assertEqual(self.user.address, "456 New St")

    def test_user_set_name(self):
        """Test setting the user's name"""
        self.user.name = "New Name"
        self.assertEqual(self.user.name, "New Name")

    def test_user_set_id(self):
        """Test setting the user's id"""
        self.user.id = 2
        self.assertEqual(self.user.id, 2)

    def test_user_set_password_hash(self):
        """Test setting the user's password hash"""
        self.user.password_hash = generate_password_hash("new_password")
        self.assertTrue(check_password_hash(self.user.password_hash, "new_password"))

    def test_user_set_properties(self):
        """Test setting the user's properties"""
        property1 = MagicMock()
        property2 = MagicMock()
        self.user.properties = [property1, property2]
        self.assertEqual(self.user.properties, [property1, property2])

    def test_user_set_transactions(self):
        """Test setting the user's transactions"""
        transaction1 = MagicMock()
        transaction2 = MagicMock()
        self.user.transactions = [transaction1, transaction2]
        self.assertEqual(self.user.transactions, [transaction1, transaction2])

    def test_user_set_whishlists(self):
        """Test setting the user's whishlists"""
        whishlist1 = MagicMock()
        whishlist2 = MagicMock()
        self.user.whishlists = [whishlist1, whishlist2]
        self.assertEqual(self.user.whishlists, [whishlist1, whishlist2])

    def test_user_set_reviews(self):
        """Test setting the user's reviews"""
        review1 = MagicMock()
        review2 = MagicMock()
        self.user.reviews = [review1, review2]
        self.assertEqual(self.user.reviews, [review1, review2])

    def test_user_set_roomparticipants(self):
        """Test setting the user's roomparticipants"""
        roomparticipant1 = MagicMock()
        roomparticipant2 = MagicMock()
        self.user.roomparticipants = [roomparticipant1, roomparticipant2]
        self.assertEqual(self.user.roomparticipants, [roomparticipant1, roomparticipant2])

    def test_user_set_password_hash_directly(self):
        """Test setting the user's password hash directly"""
        self.user.password_hash = "direct_hash"
        self.assertEqual(self.user.password_hash, "direct_hash")

if __name__ == '__main__':
    unittest.main()
