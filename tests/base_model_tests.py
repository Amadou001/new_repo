import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.base_model = BaseModel()
        self.base_model.created_at = datetime(2023, 1, 1, 12, 0, 0)
        self.base_model.updated_at = datetime(2023, 1, 2, 12, 0, 0)

    def tearDown(self):
        """Tear down test environment"""
        del self.base_model

    def test_id(self):
        """Test the id attribute"""
        self.assertIsNotNone(self.base_model.id)

    def test_created_at(self):
        """Test the created_at attribute"""
        self.assertEqual(self.base_model.created_at, datetime(2023, 1, 1, 12, 0, 0))

    def test_updated_at(self):
        """Test the updated_at attribute"""
        self.assertEqual(self.base_model.updated_at, datetime(2023, 1, 2, 12, 0, 0))

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary"""
        self.assertIsInstance(self.base_model.to_dict(), dict)

    def test_to_dict_created_at_format(self):
        """Test the format of created_at in to_dict"""
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['created_at'], '2023-01-01T12:00:00')

    def test_to_dict_updated_at_format(self):
        """Test the format of updated_at in to_dict"""
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['updated_at'], '2023-01-02T12:00:00')

    def test_to_dict_contains_id(self):
        """Test that to_dict contains id"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn('id', base_model_dict)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn('__class__', base_model_dict)

    def test_to_dict_contains_created_at(self):
        """Test that to_dict contains created_at"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn('created_at', base_model_dict)

    def test_to_dict_contains_updated_at(self):
        """Test that to_dict contains updated_at"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn('updated_at', base_model_dict)

    def test_delete_method(self):
        """Test the delete method"""
        with patch('models.storage') as mock_storage:
            self.base_model.delete()
            self.assertTrue(mock_storage.delete.called)

    def test_to_dict_includes_all_attributes(self):
        """Test that to_dict includes all attributes"""
        self.base_model.name = "Test"
        base_model_dict = self.base_model.to_dict()
        self.assertIn('name', base_model_dict)

    def test_to_dict_includes_custom_attributes(self):
        """Test that to_dict includes custom attributes"""
        self.base_model.custom_attr = "Custom"
        base_model_dict = self.base_model.to_dict()
        self.assertIn('custom_attr', base_model_dict)

    def test_to_dict_excludes_sa_instance_state(self):
        """Test that to_dict excludes _sa_instance_state"""
        self.base_model._sa_instance_state = "state"
        base_model_dict = self.base_model.to_dict()
        self.assertNotIn('_sa_instance_state', base_model_dict)

    def test_to_dict_with_no_attributes(self):
        """Test to_dict with no attributes"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_to_dict_with_empty_attributes(self):
        """Test to_dict with empty attributes"""
        self.base_model.name = ""
        base_model_dict = self.base_model.to_dict()
        self.assertIn('name', base_model_dict)
        self.assertEqual(base_model_dict['name'], "")

    def test_to_dict_with_none_attributes(self):
        """Test to_dict with None attributes"""
        self.base_model.name = None
        base_model_dict = self.base_model.to_dict()
        self.assertIn('name', base_model_dict)
        self.assertIsNone(base_model_dict['name'])

    def test_to_dict_with_boolean_attributes(self):
        """Test to_dict with boolean attributes"""
        self.base_model.is_active = True
        base_model_dict = self.base_model.to_dict()
        self.assertIn('is_active', base_model_dict)
        self.assertTrue(base_model_dict['is_active'])

    def test_to_dict_with_integer_attributes(self):
        """Test to_dict with integer attributes"""
        self.base_model.age = 30
        base_model_dict = self.base_model.to_dict()
        self.assertIn('age', base_model_dict)
        self.assertEqual(base_model_dict['age'], 30)

    def test_to_dict_with_float_attributes(self):
        """Test to_dict with float attributes"""
        self.base_model.price = 19.99
        base_model_dict = self.base_model.to_dict()
        self.assertIn('price', base_model_dict)
        self.assertEqual(base_model_dict['price'], 19.99)

    def test_to_dict_with_list_attributes(self):
        """Test to_dict with list attributes"""
        self.base_model.items = [1, 2, 3]
        base_model_dict = self.base_model.to_dict()
        self.assertIn('items', base_model_dict)
        self.assertEqual(base_model_dict['items'], [1, 2, 3])

    def test_to_dict_with_dict_attributes(self):
        """Test to_dict with dict attributes"""
        self.base_model.details = {"key": "value"}
        base_model_dict = self.base_model.to_dict()
        self.assertIn('details', base_model_dict)
        self.assertEqual(base_model_dict['details'], {"key": "value"})

    def test_to_dict_with_nested_dict_attributes(self):
        """Test to_dict with nested dict attributes"""
        self.base_model.details = {"key": {"nested_key": "nested_value"}}
        base_model_dict = self.base_model.to_dict()
        self.assertIn('details', base_model_dict)
        self.assertEqual(base_model_dict['details'], {"key": {"nested_key": "nested_value"}})

    def test_to_dict_with_empty_list_attributes(self):
        """Test to_dict with empty list attributes"""
        self.base_model.items = []
        base_model_dict = self.base_model.to_dict()
        self.assertIn('items', base_model_dict)
        self.assertEqual(base_model_dict['items'], [])

    def test_to_dict_with_empty_dict_attributes(self):
        """Test to_dict with empty dict attributes"""
        self.base_model.details = {}
        base_model_dict = self.base_model.to_dict()
        self.assertIn('details', base_model_dict)
        self.assertEqual(base_model_dict['details'], {})

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        kwargs = {
            'id': '123',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'Test'
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(base_model.updated_at, datetime(2023, 1, 2, 12, 0, 0))
        self.assertEqual(base_model.name, 'Test')

    def test_init_without_kwargs(self):
        """Test initialization without kwargs"""
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_init_with_partial_kwargs(self):
        """Test initialization with partial kwargs"""
        kwargs = {
            'name': 'Test'
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.name, 'Test')
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_init_with_empty_kwargs(self):
        """Test initialization with empty kwargs"""
        kwargs = {}
        base_model = BaseModel(**kwargs)
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_init_with_invalid_date_format(self):
        """Test initialization with invalid date format"""
        kwargs = {
            'created_at': 'invalid_date'
        }
        with self.assertRaises(ValueError):
            BaseModel(**kwargs)

if __name__ == '__main__':
    unittest.main()
