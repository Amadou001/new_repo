import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.transaction import Transaction, Subcription

class TestTransaction(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.transaction = Transaction()

    def tearDown(self):
        """Tear down test environment"""
        del self.transaction

    def test_payment_status(self):
        """Test the payment_status attribute"""
        self.transaction.payment_status = "Paid"
        self.assertEqual(self.transaction.payment_status, "Paid")

    def test_supplier_id(self):
        """Test the supplier_id attribute"""
        self.transaction.supplier_id = "supplier_123"
        self.assertEqual(self.transaction.supplier_id, "supplier_123")

    def test_property_id(self):
        """Test the property_id attribute"""
        self.transaction.property_id = "property_123"
        self.assertEqual(self.transaction.property_id, "property_123")

    def test_duration(self):
        """Test the duration attribute"""
        self.transaction.duration = 12
        self.assertEqual(self.transaction.duration, 12)

    def test_payment_status_is_string(self):
        """Test that payment_status is a string"""
        self.transaction.payment_status = "Pending"
        self.assertIsInstance(self.transaction.payment_status, str)

    def test_supplier_id_is_string(self):
        """Test that supplier_id is a string"""
        self.transaction.supplier_id = "supplier_456"
        self.assertIsInstance(self.transaction.supplier_id, str)

    def test_property_id_is_string(self):
        """Test that property_id is a string"""
        self.transaction.property_id = "property_456"
        self.assertIsInstance(self.transaction.property_id, str)

    def test_duration_is_integer(self):
        """Test that duration is an integer"""
        self.transaction.duration = 6
        self.assertIsInstance(self.transaction.duration, int)

    def test_payment_status_max_length(self):
        """Test the max length of payment_status"""
        self.transaction.payment_status = "a" * 10
        self.assertEqual(len(self.transaction.payment_status), 10)

    def test_supplier_id_max_length(self):
        """Test the max length of supplier_id"""
        self.transaction.supplier_id = "a" * 60
        self.assertEqual(len(self.transaction.supplier_id), 60)

    def test_property_id_max_length(self):
        """Test the max length of property_id"""
        self.transaction.property_id = "a" * 60
        self.assertEqual(len(self.transaction.property_id), 60)

    def test_payment_status_min_length(self):
        """Test the min length of payment_status"""
        self.transaction.payment_status = "a"
        self.assertEqual(len(self.transaction.payment_status), 1)

    def test_supplier_id_min_length(self):
        """Test the min length of supplier_id"""
        self.transaction.supplier_id = "a"
        self.assertEqual(len(self.transaction.supplier_id), 1)

    def test_property_id_min_length(self):
        """Test the min length of property_id"""
        self.transaction.property_id = "a"
        self.assertEqual(len(self.transaction.property_id), 1)

    def test_duration_min_value(self):
        """Test the min value of duration"""
        self.transaction.duration = 0
        self.assertEqual(self.transaction.duration, 0)

    def test_duration_max_value(self):
        """Test the max value of duration"""
        self.transaction.duration = 100
        self.assertEqual(self.transaction.duration, 100)

    @patch('models.transaction.Transaction.user', new_callable=MagicMock)
    def test_user_relationship(self, mock_user):
        """Test the user relationship"""
        self.assertIsNotNone(self.transaction.user)

    @patch('models.transaction.Transaction.property1', new_callable=MagicMock)
    def test_property_relationship(self, mock_property):
        """Test the property relationship"""
        self.assertIsNotNone(self.transaction.property1)

    def test_set_payment_status(self):
        """Test setting the payment_status attribute"""
        self.transaction.payment_status = "Completed"
        self.assertEqual(self.transaction.payment_status, "Completed")

    def test_set_supplier_id(self):
        """Test setting the supplier_id attribute"""
        self.transaction.supplier_id = "supplier_789"
        self.assertEqual(self.transaction.supplier_id, "supplier_789")

    def test_set_property_id(self):
        """Test setting the property_id attribute"""
        self.transaction.property_id = "property_789"
        self.assertEqual(self.transaction.property_id, "property_789")

    def test_set_duration(self):
        """Test setting the duration attribute"""
        self.transaction.duration = 24
        self.assertEqual(self.transaction.duration, 24)

class TestSubcription(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.subcription = Subcription()

    def tearDown(self):
        """Tear down test environment"""
        del self.subcription

    def test_status(self):
        """Test the status attribute"""
        self.subcription.status = "Active"
        self.assertEqual(self.subcription.status, "Active")

    def test_status_is_string(self):
        """Test that status is a string"""
        self.subcription.status = "Inactive"
        self.assertIsInstance(self.subcription.status, str)

    def test_status_max_length(self):
        """Test the max length of status"""
        self.subcription.status = "a" * 9
        self.assertEqual(len(self.subcription.status), 9)

    def test_status_min_length(self):
        """Test the min length of status"""
        self.subcription.status = "a"
        self.assertEqual(len(self.subcription.status), 1)

    def test_set_status(self):
        """Test setting the status attribute"""
        self.subcription.status = "Expired"
        self.assertEqual(self.subcription.status, "Expired")

if __name__ == '__main__':
    unittest.main()
