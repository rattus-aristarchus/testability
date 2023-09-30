
import requests
from urllib.request import urlopen
from json import load


OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


def weather():
    # First, we get the IP
    response = requests.get('https://api64.ipify.org?format=json').json()
    ip_address = response["ip"]

    # Next, determine the city based on IP
    url = 'https://ipinfo.io/' + ip_address + '/json'
    response = urlopen(url)
    json = load(response)
    city = json["city"]

    # Finally, hit up a weather service for weather in that city
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


if __name__ == '__main__':
    print(weather())
