from twilio.rest import Client
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_notification(to_number, message):
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"✅ Sent to {to_number}")
    except Exception as e:
        print(f"❌ Failed to send to {to_number}: {e}")
