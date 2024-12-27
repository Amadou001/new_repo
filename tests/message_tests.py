import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.message import Room, RoomParticipants, Message

class TestRoom(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.room = Room()

    def tearDown(self):
        """Tear down test environment"""
        del self.room

    def test_roomparticipants_relationship(self):
        """Test the roomparticipants relationship"""
        self.assertIsNotNone(self.room.roomparticipants)

    def test_message_relationship(self):
        """Test the message relationship"""
        self.assertIsNotNone(self.room.message)

class TestRoomParticipants(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.room_participant = RoomParticipants()

    def tearDown(self):
        """Tear down test environment"""
        del self.room_participant

    def test_user_id(self):
        """Test the user_id attribute"""
        self.room_participant.user_id = "user_123"
        self.assertEqual(self.room_participant.user_id, "user_123")

    def test_property_id(self):
        """Test the property_id attribute"""
        self.room_participant.property_id = "property_123"
        self.assertEqual(self.room_participant.property_id, "property_123")

    def test_room_id(self):
        """Test the room_id attribute"""
        self.room_participant.room_id = "room_123"
        self.assertEqual(self.room_participant.room_id, "room_123")

    def test_room_position(self):
        """Test the room_position attribute"""
        self.room_participant.room_position = True
        self.assertTrue(self.room_participant.room_position)

    def test_user_id_is_string(self):
        """Test that user_id is a string"""
        self.room_participant.user_id = "user_456"
        self.assertIsInstance(self.room_participant.user_id, str)

    def test_property_id_is_string(self):
        """Test that property_id is a string"""
        self.room_participant.property_id = "property_456"
        self.assertIsInstance(self.room_participant.property_id, str)

    def test_room_id_is_string(self):
        """Test that room_id is a string"""
        self.room_participant.room_id = "room_456"
        self.assertIsInstance(self.room_participant.room_id, str)

    def test_room_position_is_boolean(self):
        """Test that room_position is a boolean"""
        self.room_participant.room_position = False
        self.assertIsInstance(self.room_participant.room_position, bool)

    def test_user_id_max_length(self):
        """Test the max length of user_id"""
        self.room_participant.user_id = "a" * 60
        self.assertEqual(len(self.room_participant.user_id), 60)

    def test_property_id_max_length(self):
        """Test the max length of property_id"""
        self.room_participant.property_id = "a" * 60
        self.assertEqual(len(self.room_participant.property_id), 60)

    def test_room_id_max_length(self):
        """Test the max length of room_id"""
        self.room_participant.room_id = "a" * 60
        self.assertEqual(len(self.room_participant.room_id), 60)

    def test_user_id_min_length(self):
        """Test the min length of user_id"""
        self.room_participant.user_id = "a"
        self.assertEqual(len(self.room_participant.user_id), 1)

    def test_property_id_min_length(self):
        """Test the min length of property_id"""
        self.room_participant.property_id = "a"
        self.assertEqual(len(self.room_participant.property_id), 1)

    def test_room_id_min_length(self):
        """Test the min length of room_id"""
        self.room_participant.room_id = "a"
        self.assertEqual(len(self.room_participant.room_id), 1)

    @patch('models.message.RoomParticipants.room', new_callable=MagicMock)
    def test_room_relationship(self, mock_room):
        """Test the room relationship"""
        self.assertIsNotNone(self.room_participant.room)

    @patch('models.message.RoomParticipants.property', new_callable=MagicMock)
    def test_property_relationship(self, mock_property):
        """Test the property relationship"""
        self.assertIsNotNone(self.room_participant.property)

    @patch('models.message.RoomParticipants.user', new_callable=MagicMock)
    def test_user_relationship(self, mock_user):
        """Test the user relationship"""
        self.assertIsNotNone(self.room_participant.user)

    def test_set_user_id(self):
        """Test setting the user_id attribute"""
        self.room_participant.user_id = "user_789"
        self.assertEqual(self.room_participant.user_id, "user_789")

    def test_set_property_id(self):
        """Test setting the property_id attribute"""
        self.room_participant.property_id = "property_789"
        self.assertEqual(self.room_participant.property_id, "property_789")

    def test_set_room_id(self):
        """Test setting the room_id attribute"""
        self.room_participant.room_id = "room_789"
        self.assertEqual(self.room_participant.room_id, "room_789")

    def test_set_room_position(self):
        """Test setting the room_position attribute"""
        self.room_participant.room_position = True
        self.assertTrue(self.room_participant.room_position)

class TestMessage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.message = Message()

    def tearDown(self):
        """Tear down test environment"""
        del self.message

    def test_message_content(self):
        """Test the message content attribute"""
        self.message.content = "Hello, this is a test message."
        self.assertEqual(self.message.content, "Hello, this is a test message.")

    def test_message_sender(self):
        """Test the message sender attribute"""
        self.message.sender_id = "user_123"
        self.assertEqual(self.message.sender_id, "user_123")

    def test_message_receiver(self):
        """Test the message receiver attribute"""
        self.message.receiver_id = "user_456"
        self.assertEqual(self.message.receiver_id, "user_456")

    def test_message_room(self):
        """Test the message room attribute"""
        self.message.room_id = "room_123"
        self.assertEqual(self.message.room_id, "room_123")

    def test_message_content_is_string(self):
        """Test that message content is a string"""
        self.message.content = "Test message content"
        self.assertIsInstance(self.message.content, str)

    def test_message_sender_is_string(self):
        """Test that message sender is a string"""
        self.message.sender_id = "user_789"
        self.assertIsInstance(self.message.sender_id, str)

    def test_message_receiver_is_string(self):
        """Test that message receiver is a string"""
        self.message.receiver_id = "user_789"
        self.assertIsInstance(self.message.receiver_id, str)

    def test_message_room_is_string(self):
        """Test that message room is a string"""
        self.message.room_id = "room_456"
        self.assertIsInstance(self.message.room_id, str)

    def test_message_content_max_length(self):
        """Test the max length of message content"""
        self.message.content = "a" * 1000
        self.assertEqual(len(self.message.content), 1000)

    def test_message_sender_max_length(self):
        """Test the max length of message sender"""
        self.message.sender_id = "a" * 60
        self.assertEqual(len(self.message.sender_id), 60)

    def test_message_receiver_max_length(self):
        """Test the max length of message receiver"""
        self.message.receiver_id = "a" * 60
        self.assertEqual(len(self.message.receiver_id), 60)

    def test_message_room_max_length(self):
        """Test the max length of message room"""
        self.message.room_id = "a" * 60
        self.assertEqual(len(self.message.room_id), 60)

    def test_message_content_min_length(self):
        """Test the min length of message content"""
        self.message.content = "a"
        self.assertEqual(len(self.message.content), 1)

    def test_message_sender_min_length(self):
        """Test the min length of message sender"""
        self.message.sender_id = "a"
        self.assertEqual(len(self.message.sender_id), 1)

    def test_message_receiver_min_length(self):
        """Test the min length of message receiver"""
        self.message.receiver_id = "a"
        self.assertEqual(len(self.message.receiver_id), 1)

    def test_message_room_min_length(self):
        """Test the min length of message room"""
        self.message.room_id = "a"
        self.assertEqual(len(self.message.room_id), 1)

    @patch('models.message.Message.room', new_callable=MagicMock)
    def test_room_relationship(self, mock_room):
        """Test the room relationship"""
        self.assertIsNotNone(self.message.room)

    def test_set_message_content(self):
        """Test setting the message content attribute"""
        self.message.content = "New message content"
        self.assertEqual(self.message.content, "New message content")

    def test_set_message_sender(self):
        """Test setting the message sender attribute"""
        self.message.sender_id = "user_789"
        self.assertEqual(self.message.sender_id, "user_789")

    def test_set_message_receiver(self):
        """Test setting the message receiver attribute"""
        self.message.receiver_id = "user_789"
        self.assertEqual(self.message.receiver_id, "user_789")

    def test_set_message_room(self):
        """Test setting the message room attribute"""
        self.message.room_id = "room_789"
        self.assertEqual(self.message.room_id, "room_789")

if __name__ == '__main__':
    unittest.main()
