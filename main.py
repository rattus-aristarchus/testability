
import requests
from urllib.request import urlopen
from json import load


OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


def local_weather():
    """Return a string telling the local weather"""

    city = get_city()

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


def get_city():
    """Get user's city based on their IP"""

    ip_address = get_ip()
    url = 'https://ipinfo.io/' + ip_address + '/json'
    response = requests.get(url).json()
    return response["city"]


def get_ip():
    """Get user's IP"""

    url = 'https://api64.ipify.org?format=json'
    response = requests.get(url).json()
    return response["ip"]


if __name__ == '__main__':
    print(local_weather())
