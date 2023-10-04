
import requests


OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"


def run():
    ip = fetch_ip()
    city = fetch_city(ip)
    weather = fetch_local_weather(city)
    print(weather)


def fetch_local_weather(city):
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


def fetch_city(ip):
    """Get user's city based on their IP"""

    url = 'https://ipinfo.io/' + ip + '/json'
    response = requests.get(url).json()
    return response["city"]


def fetch_ip():
    """Get user's IP"""

    url = 'https://api64.ipify.org?format=json'
    response = requests.get(url).json()
    return response["ip"]


if __name__ == '__main__':
    run()
