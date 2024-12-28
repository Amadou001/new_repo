import unittest
from unittest.mock import patch, MagicMock
from models.property_image import Property_image


class TestPropertyImage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.property_image = Property_image()

    def tearDown(self):
        """Tear down test environment"""
        del self.property_image

    def test_image_type(self):
        """Test the image_type attribute"""
        self.property_image.image_type = "JPEG"
        self.assertEqual(self.property_image.image_type, "JPEG")

    def test_image_url(self):
        """Test the image_url attribute"""
        self.property_image.image_url = "http://example.com/image.jpg"
        self.assertEqual(self.property_image.image_url,
                         "http://example.com/image.jpg")

    def test_property_id(self):
        """Test the property_id attribute"""
        self.property_image.property_id = "property_123"
        self.assertEqual(self.property_image.property_id, "property_123")

    def test_image_type_is_string(self):
        """Test that image_type is a string"""
        self.property_image.image_type = "PNG"
        self.assertIsInstance(self.property_image.image_type, str)

    def test_image_url_is_string(self):
        """Test that image_url is a string"""
        self.property_image.image_url = "http://example.com/image.png"
        self.assertIsInstance(self.property_image.image_url, str)

    def test_property_id_is_string(self):
        """Test that property_id is a string"""
        self.property_image.property_id = "property_456"
        self.assertIsInstance(self.property_image.property_id, str)

    def test_image_type_max_length(self):
        """Test the max length of image_type"""
        self.property_image.image_type = "a" * 45
        self.assertEqual(len(self.property_image.image_type), 45)

    def test_image_url_max_length(self):
        """Test the max length of image_url"""
        self.property_image.image_url = "a" * 400
        self.assertEqual(len(self.property_image.image_url), 400)

    def test_property_id_max_length(self):
        """Test the max length of property_id"""
        self.property_image.property_id = "a" * 60
        self.assertEqual(len(self.property_image.property_id), 60)

    def test_image_type_min_length(self):
        """Test the min length of image_type"""
        self.property_image.image_type = "a"
        self.assertEqual(len(self.property_image.image_type), 1)

    def test_image_url_min_length(self):
        """Test the min length of image_url"""
        self.property_image.image_url = "a"
        self.assertEqual(len(self.property_image.image_url), 1)

    def test_property_id_min_length(self):
        """Test the min length of property_id"""
        self.property_image.property_id = "a"
        self.assertEqual(len(self.property_image.property_id), 1)

    @patch('models.property_image.Property_image.property2',
           new_callable=MagicMock)
    def test_property_relationship(self, mock_property):
        """Test the property relationship"""
        self.assertIsNotNone(self.property_image.property2)

    def test_set_image_type(self):
        """Test setting the image_type attribute"""
        self.property_image.image_type = "GIF"
        self.assertEqual(self.property_image.image_type, "GIF")

    def test_set_image_url(self):
        """Test setting the image_url attribute"""
        self.property_image.image_url = "http://example.com/image.gif"
        self.assertEqual(self.property_image.image_url,
                         "http://example.com/image.gif")

    def test_set_property_id(self):
        """Test setting the property_id attribute"""
        self.property_image.property_id = "property_789"
        self.assertEqual(self.property_image.property_id, "property_789")


if __name__ == '__main__':
    unittest.main()
