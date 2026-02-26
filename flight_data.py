class FlightData:

    def __init__(self, price, departure_airport, destination_airport, departure_date, return_date):
        self.price = price
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date

def find_cheapest_flight(data):
    if data is None or not data["data"]:
        print("No flight data")
        return FlightData("N/A", "N/A","N/A","N/A","N/A")

    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    departure = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    ## Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, departure, destination, departure_date, return_date)

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