
import requests


OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


def local_weather():
    # First, get the IP
    url = 'https://api64.ipify.org?format=json'
    response = requests.get(url).json()
    ip_address = response["ip"]

    # Using the IP, determine the city
    url = 'https://ipinfo.io/' + ip_address + '/json'
    response = requests.get(url).json()
    city = response["city"]

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
    print(local_weather())
