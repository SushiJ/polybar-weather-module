#!/bin/env python3

import requests
import subprocess
from datetime import datetime

from utils.icons import ICONS
from utils.io_helper import get_data
from utils.exceptions import WeatherApiException


API_KEY = ''
CITY = ''
BASE = "https://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"


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
    format = f"{icon} | {temp_data} | {humidity}% "
    print(format)


def is_wifi_connected():
    result = subprocess.run(['iwconfig'], capture_output=True, text=True)
    output = result.stdout

    # Check if any wireless interface is connected
    return 'ESSID:off/any' not in output


if __name__ == "__main__":
    if is_wifi_connected():
        set_api_key()
        request_api_data()
    else:
        print("Wifi Down")
