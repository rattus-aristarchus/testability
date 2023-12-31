import requests

OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


def fetch_ip():
    """Get user's IP from ipify"""

    url = 'https://api64.ipify.org?format=json'
    response = requests.get(url).json()
    return response["ip"]


def fetch_city(ip):
    """Get user's city based on their IP from ipinfo"""

    url = 'https://ipinfo.io/' + ip + '/json'
    response = requests.get(url).json()
    return response["city"]


def fetch_local_weather(city):
    """Get the weather in a particular city from openweathermap"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          city + \
          '&units=metric&lang=ru&appid=' + \
          OPENWEATHERMAP_APPID
    return requests.get(url).json()
