import requests
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(os.getenv("SHEETY_ENDPOINT"))
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url="ENDPOINT",
                json=new_data
            )
            print(response.text)




