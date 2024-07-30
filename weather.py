# This script will pull weather data from the internet given the user's location

import requests
import json

def get_weather():

    get_location = requests.get("https://ipinfo.io/loc")

    location = get_location.text.strip()

    lat = location.split(",")[0]
    lon = location.split(",")[1]

    current_weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,cloud_cover&daily=precipitation_probability_max&temperature_unit=fahrenheit&precipitation_unit=inch")
    
    with open("weather.json", "w") as file:
        json.dump(current_weather.json(), file)

    temperature = current_weather.json()["current"]["temperature_2m"]
    precipitation_probability_list = current_weather.json()["daily"]["precipitation_probability_max"]
    precipitation_probability = precipitation_probability_list[0]
    cloud_cover = current_weather.json()["current"]["cloud_cover"]

   
    return {"temperature": temperature, "precipitation_probability": precipitation_probability, "cloud_cover": cloud_cover}
    

get_weather()