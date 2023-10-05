import requests
from typing import Callable

OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


def tell_weather(fetch_ip: Callable[[], str],
                 fetch_city: Callable[[str], str],
                 fetch_weather: Callable[[str], str]):
    """Prints current weather at user's location."""

    ip = fetch_ip()
    city = fetch_city(ip)
    weather = fetch_weather(city)
    return weather


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


def city_ipinfo(ip: str):
    """Get user's city based on their IP"""

    url = 'https://ipinfo.io/' + ip + '/json'
    response = requests.get(url).json()
    return response["city"]


def ip_ipify():
    """Get user's IP"""

    url = 'https://api64.ipify.org?format=json'
    response = requests.get(url).json()
    return response["ip"]


if __name__ == '__main__':
    print(tell_weather(ip_ipify, city_ipinfo, weather_openweathermap))
