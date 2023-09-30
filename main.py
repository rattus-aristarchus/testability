
import requests
from urllib.request import urlopen
from json import load


def weather(city):
    """Return a string telling the weather in a particular city"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          city + \
          '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

    weather_data = requests.get(url).json()

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    msg = (f"Temperature in {city}: {str(temperature)} °C\n"
           f"Feels like {str(temperature_feels)} °C")
    return msg


def get_ip():
    """Get user's IP"""

    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_city(ip):
    """Get user's city based on their IP"""

    ip_address = ip
    url = 'https://ipinfo.io/' + ip_address + '/json'
    response = urlopen(url)
    json = load(response)
    return json["city"]


if __name__ == '__main__':
    print(weather(get_city(get_ip())))

