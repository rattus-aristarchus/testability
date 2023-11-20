import os
import datetime

import yaml

import requests

OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEASUREMENTS = os.path.join(BASE_DIR, "measurements.yml")


def local_weather():
    # First, get the IP
    url = 'https://api64.ipify.org?format=json'
    response = requests.get(url).json()
    ip_address = response["ip"]

    # Using the IP, determine the city
    url = 'https://ipinfo.io/' + ip_address + '/json'
    response = requests.get(url).json()
    city = response["city"]

    # Hit up a weather service for weather in that city
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          city + \
          '&units=metric&lang=ru&appid=' + \
          OPENWEATHERMAP_APPID
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    # If past measurements have already been taken, compare them to current results
    has_previous = False
    history = []
    if os.path.exists(MEASUREMENTS):
        history = yaml.safe_load(open(MEASUREMENTS, "r"))
        for record in reversed(history):
            if record["city"] == city:
                has_previous = True
                last_date = record["date"]
                last_temp = record["temp"]
                last_feels = record["feels"]
                diff = temperature - last_temp
                diff_feels = temperature_feels - last_feels
                break

    # Write down the current result
    with open(MEASUREMENTS, "w") as file:
        record = {"city": city,
                  "date": datetime.datetime.now().date(),
                  "temp": temperature,
                  "feels": temperature_feels}
        history.append(record)
        yaml.dump(history, file)

    # Print the result
    msg = (f"Temperature in {city}: {str(temperature)} °C"
           f"\nFeels like {str(temperature_feels)} °C")
    if has_previous:
        msg += (f"\nLast measurement taken on {last_date}"
                f"\nDifference since then: {str(diff)} (feels {str(diff_feels)})")
    print(msg)


if __name__ == '__main__':
    local_weather()
