from typing import Callable

import logic
from logic import Measurement
import persistence
import web


def run():
    measurement = take_measurement(web.ip_ipify,
                                   web.city_ipinfo,
                                   web.weather_openweathermap,
                                   logic.make_measurement)
    last_measurement = io(measurement,
                          persistence.read_history,
                          logic.extract_last_measurement,
                          logic.update_history,
                          persistence.write_history)
    output(measurement,
           last_measurement,
           logic.form_message,
           print)


def take_measurement(fetch_ip: Callable[[], str],
                     fetch_city: Callable[[str], str],
                     fetch_weather: Callable[[str], dict],
                     make_measurement: Callable[[str, dict], Measurement]):
    ip = fetch_ip()
    city = fetch_city(ip)
    data = fetch_weather(city)
    return make_measurement(city, data)


def io(measurement: Measurement,
       read_history: Callable[[], list],
       extract_last_measurement: Callable[[list], Measurement],
       update_history: Callable[[list, Measurement], list],
       write_history: Callable[[list], None]):
    history = read_history()
    last_measurement = extract_last_measurement(history)
    history = update_history(history, measurement)
    write_history(history)
    return last_measurement


def output(measurement: Measurement,
           last_measurement: Measurement,
           form_message: Callable[[Measurement, Measurement], str],
           send_message: Callable[[str], None]):
    message = form_message(measurement, last_measurement)
    send_message(message)


if __name__ == '__main__':
    run()
