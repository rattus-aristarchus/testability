
import requests


def weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          city + \
          '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

    #appid надо поменять

    weather_data = requests.get(url).json()

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    msg = f"Сейчас в городе {city} {str(temperature)} °C\nОщущается как {str(temperature_feels)} °C"
    return msg


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


"""
def get_city():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    return response.get("city")
"""


def get_city():
    from urllib.request import urlopen
    from json import load

    ip_address = get_ip()
    url = 'https://ipinfo.io/' + ip_address + '/json'
    res = urlopen(url)
    # response from url(if res==None then check connection)
    data = load(res)
    # will load the json response into data
    return data["city"]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(weather(get_city()))
