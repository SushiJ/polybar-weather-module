#!/bin/env python3
import requests
from math import ceil
from utils.io_helper import get_data


API_KEY = ''
CITY = ''
BASE = "https://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"
ICONS = {
    "Clear": '',
    "Clouds": '',
    "Rain": '',
    "Thunderstorm": '',
    "Snow": '',
    "Drizzle": '',
    "Mist": '',
    "Haze": ''
}


def get_api():
    global API_KEY, CITY
    API_KEY, CITY = get_data()


def request_api_data():
    request_url = f"{BASE}"
    parameters = {"q": CITY, "units": UNITS, "APPID": API_KEY}
    geolocation_data = requests.get(request_url, parameters)
    geolocation_json = geolocation_data.json()
    main_data = ceil(geolocation_json["main"]["temp"])
    icon_data = geolocation_json["weather"][0]["main"]
    icon = ICONS[icon_data]
    format = f"{main_data} | {icon} "
    print(format)


def get_icon(condition):
    icon = ICONS[condition]
    return icon


if __name__ == "__main__":
    get_api()
    request_api_data()
