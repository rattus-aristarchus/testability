import os
import datetime

import requests
import yaml

OPENWEATHERMAP_APPID = "79d1ca96933b0328e1c7e3e7a26cb347"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEASUREMENTS = os.path.join(BASE_DIR, "measurements.yml")


def run():
    ip = fetch_ip()
    city = fetch_city(ip)
    data = fetch_local_weather(city)
    temp, temp_feels = extract_temperature(data)
    measurements = read_measurements()
    date, last_temp, last_feels = extract_last_measurement(measurements)
    new_measurements = update_measurements(temp, temp_feels, measurements)
    write_measurements(new_measurements)
    diff, diff_feels = calc_diff(temp, temp_feels, last_temp, last_feels)
    print_message(city, temp, temp_feels, diff, diff_feels, date)


def fetch_local_weather(city):
    """Return a string telling the weather in a particular city"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          city + \
          '&units=metric&lang=ru&appid=' + \
          OPENWEATHERMAP_APPID
    return requests.get(url).json()


def extract_temperature(weather_data):
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    return temperature, temperature_feels


def print_message(city, temp, temp_feels, diff, diff_feels, last_date):
    msg = (f"Temperature in {city}: {str(temp)} °C"
           f"\nFeels like {str(temp_feels)} °C")
    if (diff is not None and
            diff_feels is not None and
            last_date is not None):
        msg += (f"\nLast measurement taken on {last_date}"
                f"\nDifference since then: {str(diff)} (feels {str(diff_feels)})")
    print(msg)


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


def read_measurements():
    result = []
    if os.path.exists(MEASUREMENTS):
        result = yaml.safe_load(open(MEASUREMENTS, "r"))
    return result


def extract_last_measurement(measurements):
    measure_date = None
    last_temp = None
    last_feels = None
    if measurements:
        measure_date = measurements[-1]["date"]
        last_temp = measurements[-1]["temp"]
        last_feels = measurements[-1]["feels"]
    return measure_date, last_temp, last_feels


def calc_diff(temp, feels, last_temp, last_feels):
    if last_temp is None or last_feels is None:
        return None, None
    else:
        return temp - last_temp, feels - last_feels


def update_measurements(temp, temp_feels, measurements):
    record = {"date": datetime.datetime.now().date(),
              "temp": temp,
              "feels": temp_feels}
    measurements.append(record)
    return measurements


def write_measurements(measurements):
    with open(MEASUREMENTS, "w") as file:
        yaml.dump(measurements, file)


if __name__ == '__main__':
    run()
