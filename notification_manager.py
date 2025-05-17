import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.client = Client("TWILO_SID", "TWILO_AUTH_TOKEN")

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_ = f"whatsapp:{os.getenv("TWILIO_WHATSAPP_NUMBER")}",
            body = message_body,
            to = f"whatsapp:{os.getenv("TWILIO_VERIFIED_NUMBER")}"
        )
        print(message.sid)

