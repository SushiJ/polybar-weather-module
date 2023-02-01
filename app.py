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


def set_api_key():
    global API_KEY, CITY
    API_KEY, CITY = get_data()


def get_data_from_api():
    request_url = f"{BASE}"
    parameters = {"q": CITY, "units": UNITS, "APPID": API_KEY}
    data = requests.get(request_url, parameters)
    json_data = data.json()
    return json_data


def get_temp_data(json):
    return ceil(json["main"]["temp"])


def get_humidity(json):
    return json["main"]["humidity"]


def request_api_data():
    json_data = get_data_from_api()
    temp_data = get_temp_data(json_data)
    icon = get_icon(json_data)
    humidity = get_humidity(json_data)
    format = f"{temp_data} | {icon}  | {humidity}"
    print(format)


def get_icon(json):
    condition = json["weather"][0]["main"]
    icon = ICONS[condition]
    return icon


if __name__ == "__main__":
    set_api_key()
    request_api_data()
