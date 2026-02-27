import requests
from dotenv import load_dotenv
import os
from typing import Dict, List, Any

load_dotenv()

class DataManager:
    """
    Handle data of the connected spreadsheet via Sheety API
    """

    SHEETY_GET_ENDPOINT = "https://api.sheety.co/231e3d5f05ab41273c22ec78074b5138/bestFlightDealProjectFlightTicketWishList/prices"
    SHEETY_PUT_ENDPOINT = "https://api.sheety.co/231e3d5f05ab41273c22ec78074b5138/bestFlightDealProjectFlightTicketWishList/prices"

    def __init__(self):
        self.destination_data = []

    def get_destination_data(self) -> List[Dict[str, Any]]:
        """
        Read from the spreadsheet and retrieve the current data via SHEETY API
        """
        header = {
            "Authorization": f"Bearer {os.getenv("SHEETY_TOKEN")}"
        }
        response = requests.get(self.SHEETY_GET_ENDPOINT, headers=header)
        data = response.json()

        print("DESTINATION DATA: ", data)
        if "prices" not in data:
            raise Exception(f"Sheety error: {data}")

        ### Insert the (whole) retrieved spreadsheet data into the destination_data dict
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        headers = {
            "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
        }

        for city in self.destination_data:
            object_id = city["id"]
            print("OBJECT ID: ", object_id)
            new_data = {
                "price": {
                    "arrivalCode": city["arrivalCode"]
                }
            }

            response = requests.put(
                url=f"{self.SHEETY_PUT_ENDPOINT}/{object_id}",
                json=new_data,
                headers=headers
            )
            print(response.text)




