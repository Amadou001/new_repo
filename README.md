# Roofmarket PROJECT
 
* ![roofmarket](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5VW1Zz5XXfcM3il2w1HcQUiq37zh-aaUyUQ&s)



create Property title="Fella Urban House" property_type="Office" price=45522 listing_type="rent" address="532 Street" city="New York" countr="USA" area=45236 bedrooms=6 bathrooms= user_id="59747c01-9246-4b7d-968d-2fbaf1260ff4"
[text](<../Archive/last one/property_listing.html>)


create Property title="Antoine House" property_type="House" price=85688 listing_type="Sell" address="856 avenue" city="London" country="United Kingdon" bathrooms=6 bedrooms=9 area=5263 user_id="6769db0e-7c53-4c49-aa22-018e03de5901"



curl -X POST http://127.0.0.1:5000/auth/payment_confirmation_api -H "Content-Type: application/json"      -d '{"property_id": "00e7e81d-ee42-4a4b-a86b-493e80a3c0a7", "supplier_id": "6769db0e-7c53-4c49-aa22-018e03de5901", "payment_status": "Done"}

curl -X POST http://127.0.0.1:5000/auth/new_conversation -H "Content-Type: application/json"      -d '{"current_user_id": "dd037241-cfad-4cad-9c4b-82369a892199", "room_id": "98d44935-5bfa-42ac-b2a0-9d9f29b6a942", "property_id": "59747c01-9246-4b7d-968d-2fbaf1260ff4", "receiver_id": "7d301c4d-b93d-4edc-b6e2-7e876a7d2106"}

CREATE EVENT IF NOT EXISTS decrease_duration_event
ON SCHEDULE EVERY 1 DAY
DO
  UPDATE `transaction`
  SET `duration` = `duration` - 1,
      `updated_at` = NOW()
  WHERE `duration` > 0;
* should stop count when the status is suspended
* Before inserting new images in agent table drop old ones


        # Example property and messages data
        property_name = "Golden Urban House"
        messages = [
            {
                "sender": True,  # True means the message is sent by the current user
                "sender_name": "John Doe",
                "text": "Hey! How are you doing today?",
                "sender_image": "",  # Not required for the sender message
                "timestamp": datetime.now()  # Use a datetime object for timestamp
            },
            {
                "sender": False,  # False means the message is from the receiver
                "sender_name": "Jane Smith",
                "text": "I'm doing well! Thank you for asking.",
                "sender_image": "img/team-1.jpg",  # Image of the receiver
                "timestamp": datetime.now()  # Use a datetime object for timestamp
            }
        ]
        room_id = "1"

* Put trigger to set the value read_status to true when the last message is updated to true 