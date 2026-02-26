import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    def __init__(self):
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_ = f"whatsapp:{os.getenv("TWILIO_WHATSAPP_SENDER_NUMBER")}",
            to = f"whatsapp:{os.getenv("TWILIO_WHATSAPP_RECIPIENT_NUMBER")}",
            body=message_body
        )
        print("MESSAGE SID: ", message.sid)

