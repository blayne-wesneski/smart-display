# This script will pull weather data from the internet given the user's location

import requests
import json


def get_weather():

    get_location = requests.get("https://ipinfo.io/loc")

    lat = get_location.text.split(",")[0]
    lon = get_location.text.split(",")[1]

    current_weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,precipitation&temperature_unit=fahrenheit&precipitation_unit=inch".format(lat=lat, lon=lon))

    with open('C:/Users/bwesneski/Desktop/Repo/smart-display/weather.json', 'w') as file:
        json.dump(current_weather.json(), file)

get_weather()