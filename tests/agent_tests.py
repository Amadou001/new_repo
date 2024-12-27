import unittest
import sys
import os
import uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.agent import Agent

class TestAgent(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.agent = Agent()

    def tearDown(self):
        """Tear down test environment"""
        del self.agent

    def test_agent_name(self):
        """Test the agent_name attribute"""
        self.agent.agent_name = "John Doe"
        self.assertEqual(self.agent.agent_name, "John Doe")

    def test_image_url(self):
        """Test the image_url attribute"""
        self.agent.image_url = "http://example.com/image.jpg"
        self.assertEqual(self.agent.image_url, "http://example.com/image.jpg")

    def test_agent_name_is_string(self):
        """Test that agent_name is a string"""
        self.agent.agent_name = "Jane Doe"
        self.assertIsInstance(self.agent.agent_name, str)

    def test_image_url_is_string(self):
        """Test that image_url is a string"""
        self.agent.image_url = "http://example.com/image.png"
        self.assertIsInstance(self.agent.image_url, str)

    def test_agent_name_max_length(self):
        """Test the max length of agent_name"""
        self.agent.agent_name = "a" * 60
        self.assertEqual(len(self.agent.agent_name), 60)

    def test_image_url_max_length(self):
        """Test the max length of image_url"""
        self.agent.image_url = "a" * 60
        self.assertEqual(len(self.agent.image_url), 60)

    def test_agent_name_min_length(self):
        """Test the min length of agent_name"""
        self.agent.agent_name = "a"
        self.assertEqual(len(self.agent.agent_name), 1)

    def test_image_url_min_length(self):
        """Test the min length of image_url"""
        self.agent.image_url = "a"
        self.assertEqual(len(self.agent.image_url), 1)

    def test_set_agent_name(self):
        """Test setting the agent_name attribute"""
        self.agent.agent_name = "Agent Smith"
        self.assertEqual(self.agent.agent_name, "Agent Smith")

    def test_set_image_url(self):
        """Test setting the image_url attribute"""
        self.agent.image_url = "http://example.com/agent.jpg"
        self.assertEqual(self.agent.image_url, "http://example.com/agent.jpg")

    def test_agent_name_not_none(self):
        """Test that agent_name is not None"""
        self.agent.agent_name = "Agent Johnson"
        self.assertIsNotNone(self.agent.agent_name)

    def test_image_url_not_none(self):
        """Test that image_url is not None"""
        self.agent.image_url = "http://example.com/agent.png"
        self.assertIsNotNone(self.agent.image_url)

    def test_agent_name_empty_string(self):
        """Test setting agent_name to an empty string"""
        self.agent.agent_name = ""
        self.assertEqual(self.agent.agent_name, "")

    def test_image_url_empty_string(self):
        """Test setting image_url to an empty string"""
        self.agent.image_url = ""
        self.assertEqual(self.agent.image_url, "")

    def test_agent_name_whitespace(self):
        """Test setting agent_name to a whitespace string"""
        self.agent.agent_name = " "
        self.assertEqual(self.agent.agent_name, " ")

    def test_image_url_whitespace(self):
        """Test setting image_url to a whitespace string"""
        self.agent.image_url = " "
        self.assertEqual(self.agent.image_url, " ")

    def test_agent_name_special_characters(self):
        """Test setting agent_name to a string with special characters"""
        self.agent.agent_name = "!@#$%^&*()"
        self.assertEqual(self.agent.agent_name, "!@#$%^&*()")

    def test_image_url_special_characters(self):
        """Test setting image_url to a string with special characters"""
        self.agent.image_url = "!@#$%^&*()"
        self.assertEqual(self.agent.image_url, "!@#$%^&*()")

if __name__ == '__main__':
    unittest.main()
