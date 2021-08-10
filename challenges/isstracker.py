#!/usr/bin/env python3
import requests
import json
import datetime
import reverse_geocoder as rg

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get("http://api.open-notify.org/iss-now.json")

    # display the methods available to our new object
    print(json.dumps(resp.json(), indent=4))
    apistr = resp.json()
    localDate = datetime.datetime.fromtimestamp(apistr['timestamp'])

    latitude = apistr['iss_position']["latitude"]
    longitude = apistr['iss_position']["longitude"]
    location = rg.search((latitude, longitude))[0]["name"]
    location2 = rg.search((latitude, longitude))[0]["admin1"]

    print(f"Date Time: {localDate}")
    print(f"Connection status: {apistr['message']}")
    print(f"ISS Location: {location} ,{location2}")



if __name__ == "__main__":
    main()
