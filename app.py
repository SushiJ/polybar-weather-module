#!/bin/env python3
from datetime import datetime
import requests

from utils.io_helper import get_data
from utils.exceptions import WeatherApiException


API_KEY = ''
CITY = ''
BASE = "https://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"
ICONS = {
    "SUN": {
        "Clear": '',
        "Clouds": '',
        "Rain": '',
        "Thunderstorm": '',
        "Snow": '',
        "Drizzle": '',
        "Mist": '',
        "Haze": ''
    },
    "MOON": {
        "Clear": '',
        "Clouds": '',
        "Rain": '',
        "Thunderstorm": '',
        "Snow": '',
        "Drizzle": '',
        "Mist": '',
        "Haze": ''
    }
}


def set_api_key():
    global API_KEY, CITY
    API_KEY, CITY = get_data()


def get_data_from_api():
    request_url = f"{BASE}"
    parameters = {"q": CITY, "units": UNITS, "APPID": API_KEY}
    response = requests.get(request_url, parameters)

    if response.status_code != 200:
        raise WeatherApiException(response.status_code)

    json_data = response.json()
    return json_data


def get_temp_data(json):
    return round(json["main"]["temp"])


def get_humidity(json):
    return json["main"]["humidity"]


def type_of_icon():
    curr_time = datetime.now()
    list = str(curr_time.time()).split(':')[:2]
    Str = ''.join(list)
    if 630 < int(Str) < 1830:
        return "SUN"
    else:
        return "MOON"


def get_icon(json):
    icon_type = type_of_icon()
    condition = json["weather"][0]["main"]
    icon = ICONS[icon_type][condition]
    return icon


def request_api_data():
    json_data = get_data_from_api()
    temp_data = get_temp_data(json_data)
    icon = get_icon(json_data)
    humidity = get_humidity(json_data)
    format = f"{icon}  | {temp_data} | {humidity}% "
    print(format)


if __name__ == "__main__":
    set_api_key()
    request_api_data()
