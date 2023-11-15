from typing import Callable
from dataclasses import dataclass
import datetime

import logic
import persistence
import web


@dataclass
class Measurement:

    ip: str
    city: str
    date: datetime.date
    temperature: int
    temperature_feels: int


def run():
    measurement = take_measurement(web.ip_ipify,
                                   web.city_ipinfo,
                                   web.weather_openweathermap)
    tell_weather(
                 persistence.read_measurements,
                 persistence.write_measurements)


def take_measurement(fetch_ip: Callable[[], str],
                     fetch_city: Callable[[str], str],
                     fetch_weather: Callable[[str], dict]):
    ip = fetch_ip()
    city = fetch_city(ip)
    data = fetch_weather(city)
    temp = logic.get_temperature(data)
    temp_feels = logic.get_temperature_feels(data)
    date = datetime.datetime.now().date()
    return Measurement(ip, city, date, temp, temp_feels)


def tell_weather(
                 read_measurements: Callable[[], list],
                 write_measurements: Callable[[list], None]):
    """Prints current weather at user's location."""

    old_measurements = read_measurements()
    date, last_temp, last_feels = logic.get_last_measurement(old_measurements)
    new_measurements = logic.update_measurements(temp, temp_feels, old_measurements)
    write_measurements(new_measurements)
    diff, diff_feels = logic.calc_diff(temp, temp_feels, last_temp, last_feels)
    message = logic.form_message(city, temp, temp_feels, diff, diff_feels, date)
    print(message)


if __name__ == '__main__':
    run()
