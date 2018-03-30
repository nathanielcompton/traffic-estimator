import urllib.request
import json
import os


starting_addr = os.getenv("STARTING_ADDR")
destination_addr = os.getenv("DESTINATION_ADDR")

key = os.getenv("GOOGLE_MAPS_API_KEY")

plus_sign = "+"

URL = 'https://maps.googleapis.com/maps/api/directions/json' + \
    '?origin=' + plus_sign.join(starting_addr.split(' ')) + \
    '&destination=' + plus_sign.join(destination_addr.split(' ')) + \
    '&departure_time=now' + \
    '&traffic_model=best_guess' + \
    '&key=' + key

with urllib.request.urlopen(URL) as req:
	res = json.loads(req.read())
	duration_in_traffic = (res['routes'][0]['legs'][0]['duration_in_traffic']['text'])


if __name__ == "__main__":
    print("Destination:", destination_addr, "\n" + "Current Estimate:", duration_in_traffic)
