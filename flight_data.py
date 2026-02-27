from dataclasses import dataclass

@dataclass()
class FlightData:
    price: float
    departure_airport: str
    destination_airport: str
    departure_date: str
    return_date: str


def find_cheapest_flight(data):
    if data  is None or not data ["data"]:
        print("No flight data")
        return FlightData(0.00, "N/A","N/A","N/A","N/A")

    print("AVAILABLE FLIGHT DATA: ", data)

    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    departure_code = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_code = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    ## Initialize FlightData with the first flight for comparison with the next flights of the rest
    cheapest_flight = FlightData(
        price= lowest_price,
        departure_airport=departure_code,
        destination_airport=destination_code,
        departure_date=departure_date,
        return_date=return_date
    )

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            departure = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, departure, destination, departure_date, return_date)

            print(f"Lowest price to {destination} is ${lowest_price}")

    return cheapest_flight