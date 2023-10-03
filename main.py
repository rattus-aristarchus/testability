from typing import Callable

import requests
import city as city_provider


OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


def run(get_ip: Callable[[], str],
        get_city: Callable[[str], str],
        get_weather: Callable[[str], None]):
    """Prints current weather at user's location."""

    ip = get_ip()
    city = get_city(ip)
    weather = get_weather(city)
    print(weather)


def weather_openweathermap(city: str):
    """Return a string telling the weather in a particular city"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          city + \
          '&units=metric&lang=ru&appid=' + \
          OPENWEATHERMAP_APPID

    weather_data = requests.get(url).json()

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    msg = (f"Temperature in {city}: {str(temperature)} °C\n"
           f"Feels like {str(temperature_feels)} °C")
    return msg


def ip_ipify():
    """Get user's IP"""

    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


if __name__ == '__main__':
    run(ip_ipify, city_provider.geolocationdb, weather_openweathermap)
