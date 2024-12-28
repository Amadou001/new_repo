import unittest
from unittest.mock import patch, MagicMock
from models.property import Property


class TestProperty(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.property = Property()

    def tearDown(self):
        """Tear down test environment"""
        del self.property

    def test_title(self):
        """Test the title attribute"""
        self.property.title = "Test Title"
        self.assertEqual(self.property.title, "Test Title")

    def test_description(self):
        """Test the description attribute"""
        self.property.description = "Test Description"
        self.assertEqual(self.property.description, "Test Description")

    def test_property_type(self):
        """Test the property_type attribute"""
        self.property.property_type = "House"
        self.assertEqual(self.property.property_type, "House")

    def test_price(self):
        """Test the price attribute"""
        self.property.price = 100000.0
        self.assertEqual(self.property.price, 100000.0)

    def test_listing_type(self):
        """Test the listing_type attribute"""
        self.property.listing_type = "Sale"
        self.assertEqual(self.property.listing_type, "Sale")

    def test_address(self):
        """Test the address attribute"""
        self.property.address = "123 Test St"
        self.assertEqual(self.property.address, "123 Test St")

    def test_city(self):
        """Test the city attribute"""
        self.property.city = "Test City"
        self.assertEqual(self.property.city, "Test City")

    def test_state(self):
        """Test the state attribute"""
        self.property.state = "Test State"
        self.assertEqual(self.property.state, "Test State")

    def test_country(self):
        """Test the country attribute"""
        self.property.country = "Test Country"
        self.assertEqual(self.property.country, "Test Country")

    def test_zip_code(self):
        """Test the zip_code attribute"""
        self.property.zip_code = "12345"
        self.assertEqual(self.property.zip_code, "12345")

    def test_bedrooms(self):
        """Test the bedrooms attribute"""
        self.property.bedrooms = 3
        self.assertEqual(self.property.bedrooms, 3)

    def test_bathrooms(self):
        """Test the bathrooms attribute"""
        self.property.bathrooms = 2
        self.assertEqual(self.property.bathrooms, 2)

    def test_area(self):
        """Test the area attribute"""
        self.property.area = 1500.0
        self.assertEqual(self.property.area, 1500.0)

    def test_user_id(self):
        """Test the user_id attribute"""
        self.property.user_id = "user_123"
        self.assertEqual(self.property.user_id, "user_123")

    @patch('models.property.Property.transaction', new_callable=MagicMock)
    def test_transactions_relationship(self, mock_transactions):
        """Test the transactions relationship"""
        self.assertIsNotNone(self.property.transaction)

    @patch('models.property.Property.whishlists', new_callable=MagicMock)
    def test_whishlists_relationship(self, mock_whishlists):
        """Test the whishlists relationship"""
        self.assertIsNotNone(self.property.whishlists)

    @patch('models.property.Property.reviews', new_callable=MagicMock)
    def test_reviews_relationship(self, mock_reviews):
        """Test the reviews relationship"""
        self.assertIsNotNone(self.property.reviews)

    def test_set_title(self):
        """Test setting the title attribute"""
        self.property.title = "New Title"
        self.assertEqual(self.property.title, "New Title")

    def test_set_description(self):
        """Test setting the description attribute"""
        self.property.description = "New Description"
        self.assertEqual(self.property.description, "New Description")

    def test_set_property_type(self):
        """Test setting the property_type attribute"""
        self.property.property_type = "Apartment"
        self.assertEqual(self.property.property_type, "Apartment")

    def test_set_price(self):
        """Test setting the price attribute"""
        self.property.price = 200000.0
        self.assertEqual(self.property.price, 200000.0)

    def test_set_listing_type(self):
        """Test setting the listing_type attribute"""
        self.property.listing_type = "Rent"
        self.assertEqual(self.property.listing_type, "Rent")

    def test_set_address(self):
        """Test setting the address attribute"""
        self.property.address = "456 New St"
        self.assertEqual(self.property.address, "456 New St")

    def test_set_city(self):
        """Test setting the city attribute"""
        self.property.city = "New City"
        self.assertEqual(self.property.city, "New City")

    def test_set_state(self):
        """Test setting the state attribute"""
        self.property.state = "New State"
        self.assertEqual(self.property.state, "New State")

    def test_set_country(self):
        """Test setting the country attribute"""
        self.property.country = "New Country"
        self.assertEqual(self.property.country, "New Country")

    def test_set_zip_code(self):
        """Test setting the zip_code attribute"""
        self.property.zip_code = "67890"
        self.assertEqual(self.property.zip_code, "67890")

    def test_set_bedrooms(self):
        """Test setting the bedrooms attribute"""
        self.property.bedrooms = 4
        self.assertEqual(self.property.bedrooms, 4)

    def test_set_bathrooms(self):
        """Test setting the bathrooms attribute"""
        self.property.bathrooms = 3
        self.assertEqual(self.property.bathrooms, 3)

    def test_set_area(self):
        """Test setting the area attribute"""
        self.property.area = 2000.0
        self.assertEqual(self.property.area, 2000.0)

    def test_set_user_id(self):
        """Test setting the user_id attribute"""
        self.property.user_id = "user_456"
        self.assertEqual(self.property.user_id, "user_456")

    def test_title_is_string(self):
        """Test that title is a string"""
        self.property.title = "Test Title"
        self.assertIsInstance(self.property.title, str)

    def test_description_is_string(self):
        """Test that description is a string"""
        self.property.description = "Test Description"
        self.assertIsInstance(self.property.description, str)

    def test_property_type_is_string(self):
        """Test that property_type is a string"""
        self.property.property_type = "House"
        self.assertIsInstance(self.property.property_type, str)

    def test_price_is_float(self):
        """Test that price is a float"""
        self.property.price = 100000.0
        self.assertIsInstance(self.property.price, float)

    def test_listing_type_is_string(self):
        """Test that listing_type is a string"""
        self.property.listing_type = "Sale"
        self.assertIsInstance(self.property.listing_type, str)

    def test_address_is_string(self):
        """Test that address is a string"""
        self.property.address = "123 Test St"
        self.assertIsInstance(self.property.address, str)

    def test_city_is_string(self):
        """Test that city is a string"""
        self.property.city = "Test City"
        self.assertIsInstance(self.property.city, str)

    def test_state_is_string(self):
        """Test that state is a string"""
        self.property.state = "Test State"
        self.assertIsInstance(self.property.state, str)

    def test_country_is_string(self):
        """Test that country is a string"""
        self.property.country = "Test Country"
        self.assertIsInstance(self.property.country, str)

    def test_zip_code_is_string(self):
        """Test that zip_code is a string"""
        self.property.zip_code = "12345"
        self.assertIsInstance(self.property.zip_code, str)

    def test_bedrooms_is_integer(self):
        """Test that bedrooms is an integer"""
        self.property.bedrooms = 3
        self.assertIsInstance(self.property.bedrooms, int)

    def test_bathrooms_is_integer(self):
        """Test that bathrooms is an integer"""
        self.property.bathrooms = 2
        self.assertIsInstance(self.property.bathrooms, int)

    def test_area_is_float(self):
        """Test that area is a float"""
        self.property.area = 1500.0
        self.assertIsInstance(self.property.area, float)

    def test_user_id_is_string(self):
        """Test that user_id is a string"""
        self.property.user_id = "user_123"
        self.assertIsInstance(self.property.user_id, str)

    def test_title_max_length(self):
        """Test the max length of title"""
        self.property.title = "a" * 50
        self.assertEqual(len(self.property.title), 50)

    def test_description_max_length(self):
        """Test the max length of description"""
        self.property.description = "a" * 2050
        self.assertEqual(len(self.property.description), 2050)

    def test_property_type_max_length(self):
        """Test the max length of property_type"""
        self.property.property_type = "a" * 10
        self.assertEqual(len(self.property.property_type), 10)

    def test_listing_type_max_length(self):
        """Test the max length of listing_type"""
        self.property.listing_type = "a" * 5
        self.assertEqual(len(self.property.listing_type), 5)

    def test_address_max_length(self):
        """Test the max length of address"""
        self.property.address = "a" * 224
        self.assertEqual(len(self.property.address), 224)

    def test_city_max_length(self):
        """Test the max length of city"""
        self.property.city = "a" * 50
        self.assertEqual(len(self.property.city), 50)

    def test_state_max_length(self):
        """Test the max length of state"""
        self.property.state = "a" * 50
        self.assertEqual(len(self.property.state), 50)

    def test_country_max_length(self):
        """Test the max length of country"""
        self.property.country = "a" * 50
        self.assertEqual(len(self.property.country), 50)

    def test_zip_code_max_length(self):
        """Test the max length of zip_code"""
        self.property.zip_code = "a" * 15
        self.assertEqual(len(self.property.zip_code), 15)

    def test_title_min_length(self):
        """Test the min length of title"""
        self.property.title = "a"
        self.assertEqual(len(self.property.title), 1)

    def test_description_min_length(self):
        """Test the min length of description"""
        self.property.description = "a"
        self.assertEqual(len(self.property.description), 1)

    def test_property_type_min_length(self):
        """Test the min length of property_type"""
        self.property.property_type = "a"
        self.assertEqual(len(self.property.property_type), 1)

    def test_listing_type_min_length(self):
        """Test the min length of listing_type"""
        self.property.listing_type = "a"
        self.assertEqual(len(self.property.listing_type), 1)

    def test_address_min_length(self):
        """Test the min length of address"""
        self.property.address = "a"
        self.assertEqual(len(self.property.address), 1)

    def test_city_min_length(self):
        """Test the min length of city"""
        self.property.city = "a"
        self.assertEqual(len(self.property.city), 1)

    def test_state_min_length(self):
        """Test the min length of state"""
        self.property.state = "a"
        self.assertEqual(len(self.property.state), 1)

    def test_country_min_length(self):
        """Test the min length of country"""
        self.property.country = "a"
        self.assertEqual(len(self.property.country), 1)

    def test_zip_code_min_length(self):
        """Test the min length of zip_code"""
        self.property.zip_code = "a"
        self.assertEqual(len(self.property.zip_code), 1)

    def test_bedrooms_min_value(self):
        """Test the min value of bedrooms"""
        self.property.bedrooms = 0
        self.assertEqual(self.property.bedrooms, 0)

    def test_bathrooms_min_value(self):
        """Test the min value of bathrooms"""
        self.property.bathrooms = 0
        self.assertEqual(self.property.bathrooms, 0)

    def test_area_min_value(self):
        """Test the min value of area"""
        self.property.area = 0.0
        self.assertEqual(self.property.area, 0.0)

    def test_price_min_value(self):
        """Test the min value of price"""
        self.property.price = 0.0
        self.assertEqual(self.property.price, 0.0)

    def test_bedrooms_max_value(self):
        """Test the max value of bedrooms"""
        self.property.bedrooms = 100
        self.assertEqual(self.property.bedrooms, 100)

    def test_bathrooms_max_value(self):
        """Test the max value of bathrooms"""
        self.property.bathrooms = 100
        self.assertEqual(self.property.bathrooms, 100)

    def test_area_max_value(self):
        """Test the max value of area"""
        self.property.area = 10000.0
        self.assertEqual(self.property.area, 10000.0)

    def test_price_max_value(self):
        """Test the max value of price"""
        self.property.price = 100000000.0
        self.assertEqual(self.property.price, 100000000.0)


if __name__ == '__main__':
    unittest.main()
