import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.whishlist import Whishlist

class TestWhishlist(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.whishlist = Whishlist()

    def tearDown(self):
        """Tear down test environment"""
        del self.whishlist

    def test_user_id(self):
        """Test the user_id attribute"""
        self.whishlist.user_id = "user_123"
        self.assertEqual(self.whishlist.user_id, "user_123")

    def test_property_id(self):
        """Test the property_id attribute"""
        self.whishlist.property_id = "property_123"
        self.assertEqual(self.whishlist.property_id, "property_123")

    def test_user_id_is_string(self):
        """Test that user_id is a string"""
        self.whishlist.user_id = "user_456"
        self.assertIsInstance(self.whishlist.user_id, str)

    def test_property_id_is_string(self):
        """Test that property_id is a string"""
        self.whishlist.property_id = "property_456"
        self.assertIsInstance(self.whishlist.property_id, str)

    def test_user_id_max_length(self):
        """Test the max length of user_id"""
        self.whishlist.user_id = "a" * 60
        self.assertEqual(len(self.whishlist.user_id), 60)

    def test_property_id_max_length(self):
        """Test the max length of property_id"""
        self.whishlist.property_id = "a" * 60
        self.assertEqual(len(self.whishlist.property_id), 60)

    def test_user_id_min_length(self):
        """Test the min length of user_id"""
        self.whishlist.user_id = "a"
        self.assertEqual(len(self.whishlist.user_id), 1)

    def test_property_id_min_length(self):
        """Test the min length of property_id"""
        self.whishlist.property_id = "a"
        self.assertEqual(len(self.whishlist.property_id), 1)

    @patch('models.whishlist.Whishlist.user', new_callable=MagicMock)
    def test_user_relationship(self, mock_user):
        """Test the user relationship"""
        self.assertIsNotNone(self.whishlist.user)

    @patch('models.whishlist.Whishlist.properties', new_callable=MagicMock)
    def test_properties_relationship(self, mock_properties):
        """Test the properties relationship"""
        self.assertIsNotNone(self.whishlist.properties)

    def test_set_user_id(self):
        """Test setting the user_id attribute"""
        self.whishlist.user_id = "user_789"
        self.assertEqual(self.whishlist.user_id, "user_789")

    def test_set_property_id(self):
        """Test setting the property_id attribute"""
        self.whishlist.property_id = "property_789"
        self.assertEqual(self.whishlist.property_id, "property_789")

    def test_user_id_not_none(self):
        """Test that user_id is not None"""
        self.whishlist.user_id = "user_123"
        self.assertIsNotNone(self.whishlist.user_id)

    def test_property_id_not_none(self):
        """Test that property_id is not None"""
        self.whishlist.property_id = "property_123"
        self.assertIsNotNone(self.whishlist.property_id)

    def test_user_id_empty_string(self):
        """Test setting user_id to an empty string"""
        self.whishlist.user_id = ""
        self.assertEqual(self.whishlist.user_id, "")

    def test_property_id_empty_string(self):
        """Test setting property_id to an empty string"""
        self.whishlist.property_id = ""
        self.assertEqual(self.whishlist.property_id, "")

    def test_user_id_whitespace(self):
        """Test setting user_id to a whitespace string"""
        self.whishlist.user_id = " "
        self.assertEqual(self.whishlist.user_id, " ")

    def test_property_id_whitespace(self):
        """Test setting property_id to a whitespace string"""
        self.whishlist.property_id = " "
        self.assertEqual(self.whishlist.property_id, " ")

    def test_user_id_special_characters(self):
        """Test setting user_id to a string with special characters"""
        self.whishlist.user_id = "!@#$%^&*()"
        self.assertEqual(self.whishlist.user_id, "!@#$%^&*()")

    def test_property_id_special_characters(self):
        """Test setting property_id to a string with special characters"""
        self.whishlist.property_id = "!@#$%^&*()"
        self.assertEqual(self.whishlist.property_id, "!@#$%^&*()")

if __name__ == '__main__':
    unittest.main()
