import requests

OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


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


def weather_openweathermap(city):
    """Return a string telling the weather in a particular city"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          city + \
          '&units=metric&lang=ru&appid=' + \
          OPENWEATHERMAP_APPID
    return requests.get(url).json()
