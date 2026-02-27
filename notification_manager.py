import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    def __init__(self):
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_whatsapp(self, message_body: str):
        sender = os.getenv("TWILIO_WHATSAPP_SENDER_NUMBER")
        recipient = os.getenv("TWILIO_WHATSAPP_RECIPIENT_NUMBER")

        try:
            message = self.client.messages.create(
                from_= f"whatsapp:{sender}",
                to= f"whatsapp:{recipient}",
                body=message_body
            )
            print("WhatsApp notification sent successfully!")
            print("Current Status:", message.status)
        except Exception as e:
            print("Failed to send WhatsApp message:", e)
